int sensorPin = A0;  // photoresistors
int sensorValue = 0;
int motorLeft = 9;  // motors
int motorRight = 10;
int forRev1 = 7;  // changing motor direction (forward/reverse)
int forRev2 = 8;
int velocityLeft = 200;  // set initial motor/wheel velocities
int velocityRight = 200;

int lastTime;
int setPt;
int errorSum;
int errorLast;
int kp;
int ki;
int kd;

void setup() {
  
  //  set motors and motor directions as outputs, initial direction forward 
  pinMode(motorLeft, OUTPUT);  
  pinMode(motorRight, OUTPUT);
  pinMode(forRev1, OUTPUT);
  pinMode(forRev2, OUTPUT);
  digitalWrite(forRev1, LOW);
  digitalWrite(forRev2, LOW);
  
  setPt = analogRead(sensorPin); // color detect edge
  
  kp = 1;
  ki = 100;
  
  Serial.begin(9600);
  
}

void loop() {
  
  sensorValue = analogRead(sensorPin);
  
  velocityLeft = 100;
  velocityRight = 100;

  int now = millis();
  int timeChange = now - lastTime;
  int error = setPt - sensorValue;
  
  errorSum += (error * timeChange);
  
  if ((error) > 0) {
    velocityLeft = kp * (error + 25) + ki * errorSum;
  }
 
  if ((error) < 0) {
    velocityRight = kp * (error - 25) + ki * errorSum;
  }
  
  analogWrite(motorLeft, velocityLeft); 
  analogWrite(motorRight, velocityRight);
  
  delay(10);  //10 ms delay
  
  Serial.println(sensorValue);
  
}
