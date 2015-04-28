int sensorPin = A0;  // photoresistors
int sensorValue = 0;
int motorLeft = 9;  // motors
int motorRight = 10;
int forRev1 = 7;  // changing motor direction (forward/reverse)
int forRev2 = 8;
int velocityLeft = 200;  // set initial motor/wheel velocities
int velocityRight = 200;

int setPt;
int kp;

void setup() {
  
  //  set motors and motor directions as outputs, initial direction forward 
  pinMode(motorLeft, OUTPUT);  
  pinMode(motorRight, OUTPUT);
  pinMode(forRev1, OUTPUT);
  pinMode(forRev2, OUTPUT);
  digitalWrite(forRev1, LOW);
  digitalWrite(forRev2, LOW);
  
  setPt = analogRead(sensorPin); // color detect edge at start
  
  kp = 1;  //set a kp value
  
  Serial.begin(9600);
  
}

void loop() {
  
  sensorValue = analogRead(sensorPin);
  
  velocityLeft = 100; // reset wheel speeds
  velocityRight = 100;
  
  int error = setPt - sensorValue;
  
  //sign of error controls turning
  if (error > 0) {
    velocityLeft = kp * (error + 25);  // account for PWM not ideal
  }
 
  if (error < 0) {
    velocityRight = kp * (error - 25);
  }
  
  analogWrite(motorLeft, velocityLeft);
  analogWrite(motorRight, velocityRight);
  
  delay(10);  //10 ms delay
  
  Serial.println(sensorValue);
  
}
