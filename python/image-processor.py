from subprocess import call
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import requests
import json

endpoint = "https://ninjas-computer-vision.cognitiveservices.azure.com/"
config = json.load(open("./config.json", "r"))

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(config["computer_vision_key"]))

ingredients = json.load(open("./ingredients.json", "r"))

print("start")

call("./capture.sh", shell=True)

local_image = open("image.jpg", "rb")
local_image_features = ["objects"]
# Call API
tags_result_local = computervision_client.tag_image_in_stream(local_image)

# Print results with confidence score
#print("Tags in the local image: ")
if (len(tags_result_local.tags) == 0):
    print("No tags detected.")

matches = []

for tag in tags_result_local.tags:
    if tag.confidence > .6:
        matches.append(tag.name)
print()
print("ingredients in the picture: ")
for match in matches:
    print(match)

print()
headers = {'Content-Type': 'application/json', 'Accept':'application/json'}

r = requests.post(config["power_automate_endpoint"], data = json.dumps(matches), headers=headers )
print(r)