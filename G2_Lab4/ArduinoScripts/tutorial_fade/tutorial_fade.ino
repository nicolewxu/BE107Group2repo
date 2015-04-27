int ledPin = 13;           
int brightness = 0;    // how bright the LED is (intially dark)
int fadeAmount = 1;    // how many points to fade the LED by

void setup()  { 
  
  pinMode(ledPin, OUTPUT);  // LED pin 13 is an output

} 

void loop()  { 
  
  analogWrite(ledPin, brightness);  // set the brightness of LED pin 13
  
  // change the brightness for next time through the loop
  brightness = brightness + fadeAmount; 
  
  // reverse the direction of fading at the ends of the fade 
  if (brightness == 0 || brightness == 255) {
    fadeAmount = -fadeAmount ; 
  }     
     
  delay(200);  // wait for 200 ms to see the dimming effect    
  
}
