#include <Servo.h>
Servo myservo1;
Servo myservo2;
Servo myservo3;
Servo myservo4;
int mv1,mv2;
int pos1 = 50;
int pos2 = 50;
int pos3 = 0;
int pos4 = 30;
int maxspd=5;
int dly=100;
void setup(){
Serial.begin(9600);
myservo1.attach(9);
myservo2.attach(11);
myservo3.attach(5);
myservo4.attach(3);
pinMode(13,OUTPUT);//output for raspberry}
void loop(){
mv1= map(analogRead(A0),0,1023,(-maxspd),(macspd+1));
mv2= map(analogRead(A1),0,1023,(-maxspd),(maxspd+1));
pos1 += mv1;
pos2 += mv2;
pos3= map(analogRead(A2),0,1023,0,180);
if(pos1>180)pos1=180;
if(pos2>180)pos2=180;
if(pos1<0)pos1=0;
if(pos2<0)pos2=0;
if(digitalRead(2)==HIGH){
pos4=130;
digitalWrite(13,HIGH);
}
else{
pos4=30;
digitalWrite(13,LOW);
}
Serial.print(pos1);
Serial.print("\t");
Serial.print(pos2);
Serial.print("\t");
Serial.print(pos3);
Serial.print("\t");
Serial.println(pos4);
myservo1.write(pos1);
myservo2.write(pos2);
myservo3.write(pos3);
myservo4.write(pos4);
delay(dly);
}
