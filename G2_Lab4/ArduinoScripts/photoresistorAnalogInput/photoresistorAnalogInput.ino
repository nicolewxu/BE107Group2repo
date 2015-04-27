int sensorPinLeft = A1;    // select the input pin for the photoresistor
int ledPin = 13;      // select the pin for the LED
int sensorValueLeft = 0;  //initialize value to 0

void setup() {
 
  pinMode(ledPin, OUTPUT);  // declare the ledPin as an OUTPUT:
  
}

void loop() {
  
  sensorValueLeft = analogRead(sensorPinLeft); // read value from the photores
  
  digitalWrite(ledPin, HIGH);  // turn the ledPin on
  delay(sensorValueLeft*10);  // delay for <sensorValue> ms * 10     
         
  digitalWrite(ledPin, LOW);  // turn the ledPin off:
  delay(sensorValueLeft*10);  // delay for <sensorValue> ms * 10
  
}
