from subprocess import call
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import json

endpoint = "https://ninjas-computer-vision.cognitiveservices.azure.com/"
config = json.load(open("./config.json", "r"))

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(config["computer_vision_key"]))

#ingredients = json.load(open("./ingredients.json", "r"))

print("start")

rc = call("./capture.sh", shell=True)

print(rc)

local_image = open("image.jpg", "rb")
local_image_features = ["objects"]
# Call API
tags_result_local = computervision_client.tag_image_in_stream(local_image)

# Print results with confidence score
#print("Tags in the local image: ")
if (len(tags_result_local.tags) == 0):
    print("No tags detected.")
#else:
 #   for tag in tags_result_local.tags:
 ##       print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
print()

matches = []

for tag in tags_result_local.tags:
    if tag.confidence >= 7:
        matches.append(tag.name)

for match in matches:
    print(match)
