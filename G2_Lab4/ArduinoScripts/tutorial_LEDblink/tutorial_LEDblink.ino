int ledPin = 13;  // assign to pin 13, built-in LED

void setup() {
  
  pinMode(ledPin, OUTPUT);  // LED pin 13 is an output
  
}

void loop() {
 
  digitalWrite(ledPin, HIGH);  // LED pin 13 is on
  delay(200); // wait for 200 ms
  
  digitalWrite(ledPin,LOW);  // LED pin 13 is off
  delay(200); // wait for 200 ms
  
}
