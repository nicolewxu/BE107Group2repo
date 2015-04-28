int sensorPinLeft = A0;  // photoresistors
int sensorPinRight = A1;
int motorLeft = 9;  // motors
int motorRight = 10;
int forRev1 = 7;  // changing motor direction (forward/reverse)
int forRev2 = 8;
int sensorValueLeft = 0;  // outputs from photoresistors
int sensorValueRight = 0;
int velocityLeft = 100;  // set initial motor/wheel velocities
int velocityRight = 100;

void setup() {
  
  //  set motors and motor directions as outputs, initial direction forward 
  pinMode(motorLeft, OUTPUT);  
  pinMode(motorRight, OUTPUT);
  pinMode(forRev1, OUTPUT);
  pinMode(forRev2, OUTPUT);
  digitalWrite(forRev1, HIGH);
  digitalWrite(forRev2, HIGH);
  
  Serial.begin(9600);
}

void loop() {
  
  sensorValueLeft = analogRead(sensorPinLeft);  // assign photoresistor vals
  sensorValueRight = analogRead(sensorPinRight);
  
  //velocityLeft = sensorValueLeft;
  //velocityRight = sensorValueRight;
  
  velocityLeft = sensorValueLeft/4;    // linear mapping (divide by 4)
  velocityRight = sensorValueRight/4;
  
  /*if (sensorValueLeft > 255) {  // threshold mapping (highest value is 255)
    velocityLeft = 255;  }
  else {
    velocityLeft = sensorValueLeft;
  }
  if (sensorValueRight > 255) {
    velocityRight = 255;  }
  else {
    velocityRight = sensorValueRight;
  }*/
  
  analogWrite(motorLeft, velocityLeft);  // assign photores-dep velocities
  analogWrite(motorRight, velocityRight);  // to motors, independently
  
  delay(10);  //10 ms delay
  
  Serial.println(sensorValueLeft);    // view values of photores outputs on 
  Serial.println(sensorValueRight);
}
