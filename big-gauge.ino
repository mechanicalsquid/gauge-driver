/*Gauge Driver v1.1

mechanicalsquid 2015
*/
#include <SwitecX25.h>
String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete
boolean thismessage = false;     // whether the incoming data is for this device
static int nextPos = 0;          // the new motor position

// Total range for this gauge is 122 degrees at 3 steps.
#define STEPS (122*3)            
SwitecX25 motor1(STEPS,6,5,7,4);

void setup() {
  // initialize serial:
  Serial.begin(4800);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
  // zero motor by running against stops
  motor1.zero();
  // move to centre of range
  motor1.setPosition(STEPS/2);
}

void loop() {
  // update the motor position
  motor1.update();
  
  // do this if incoming message is complete
  if (stringComplete==true) {
      motor1.setPosition(nextPos); // set new motor position
      nextPos = 0;
    stringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read(); 
    // This gauge defined by 'b' prefix on incoming string
    if (inChar == 'b'){
      thismessage=true;
    }
    // All gauges zero themselves with '!'
    if (inChar == '!'){
      motor1.zero();
    }
    // build nextpos from each character
    if (thismessage == true && inChar>='0' && inChar<='9') {
      nextPos = 10*nextPos + (inChar-'0');
    }
    // continue until newline
    if (thismessage==true && inChar == '\n') {
      stringComplete = true;
      thismessage = false;
    } 
  }
}


