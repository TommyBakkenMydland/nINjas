#include <Stepper.h>
#include <String.h>
import pyfirmatas

const int rep = 2050
const int turn = rep
int dir = -1;
Stepper stepper = Stepper(rep,9, 11, 10, 12); //make sure this matches your setup


const int dosage = 2;



/********************* CODE *****************/

void setup() {
  
  stepper.setSpeed(10);
}

void loop() {
  Serial.begin(9600);
  dispense(dosage);
  

}

void wiggle (int times){
  for (int i = 0; i<times; i++){
    stepper.step(-100);
    delay(10);
    stepper.step(100);
  }
}

void dispense (int times){
    for (int i = 0; i<times; i++){
      Serial.println("Dispensing");
      wiggle(2);
      stepper.step(turn*dir);
      dir= dir*-1;
    }
    digitalWrite(9,LOW);
    digitalWrite(10,LOW);
    digitalWrite(11,LOW);
    digitalWrite(12,LOW);  
    Serial.println("done");
}