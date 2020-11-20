
#include <Wire.h>
#define I2C_SLAVE_ADDRESS 11

int sensor = 0;

 
void setup() {
  Serial.begin(9600);
  Wire.begin(I2C_SLAVE_ADDRESS);                // join i2c bus with address #11
  Wire.onRequest(requestEvent); // register event
  Wire.onReceive(receiveEvents);

}

void loop() {
  delay(100);
}


void requestEvent() { // if request send from raspi, we will respond with "ek"
  String response;
  char buffer[16];
  if(sensor == 1){
    response = "1s";
    }
  else if(sensor == 2){
    response = "2s";
      }
   else{
    response = "ns";
    }
  response.toCharArray(buffer, 16);
  Wire.write(buffer); 
  Serial.println("responsed");
}
void receiveEvents(int numBytes) // if some data has been recieved from raspi
{  
  String request;
  while(Wire.available()){
    int number = Wire.read();
    request = (char)number;
    Serial.println(request);
  }
  if(request == "1"){
    sensor = 1;
  }
  if(request == "2"){
    sensor = 2;
    }  
}
