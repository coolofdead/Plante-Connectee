// SparkFun APDS-9301 Lux Sensor - Version: Latest 


// thinger.io - Version: Latest 


#include "Wire.h"
    #include <Sparkfun_APDS9301_Library.h>

    APDS9301 apds;

    #define INT_PIN 2 // We'll connect the INT pin from our sensor to the
                      // INT0 interrupt pin on the Arduino.
    bool lightIntHappened = false; // flag set in the interrupt to let the
                     //  mainline code know that an interrupt occurred.
    #include "DHT.h"
                     
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

#define _DEBUG_
#define _DISABLE_TLS_
#define THINGER_USE_STATIC_MEMORY
#define THINGER_STATIC_MEMORY_SIZE 512
#define ThingerWifi ThingerWifiClient

#include <WiFi.h>
#include <ThingerWifi.h>

#define USERNAME "coolofdead"
#define DEVICE_ID "arduino"
#define DEVICE_CREDENTIAL "arduino"

#define SSID "iPhone de Thomas"
#define SSID_PASSWORD "coolofdead"

ThingerWifi thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

int temperature = 0;
int humiditeAir = 0;
int humiditeSol = 0;

void setup() {
  Serial.begin(9600);
  // configure wifi network
  thing.add_wifi(SSID, SSID_PASSWORD);



  thing["Luminosite"] >> [](pson& out){
    out["Luminosite"] = apds.readCH0Level();
  };
  
  dht.begin();
  thing["HumiditeAir"] >> [](pson& out){
    out["HumiditeAir"] = humiditeAir;
    
  };
  thing["HumiditeSol"] >> [](pson& out){
    out["HumiditeSol"] = humiditeSol;
  };
  
  
  
  dht.begin();
  thing["Temperature"] >> [](pson& out){
    out["Temperature"] = temperature;
  };
  
  
  
  
  delay(5);    // The CCS811 need  a brief delay after startup.
      Serial.begin(9600);
      Wire.begin();
    
      // APDS9301 sensor setup.
      apds.begin(0x39);  // We're assuming you haven't changed the I2C
                        //  address from the default by soldering the
                        //  jumper on the back of the board.
      apds.setGain(APDS9301::LOW_GAIN); // Set the gain to low. Strictly
                        //  speaking, this isn't necessary, as the gain
                        //  defaults to low.
      apds.setIntegrationTime(APDS9301::INT_TIME_13_7_MS); // Set the
                        //  integration time to the shortest interval.
                        //  Again, not strictly necessary, as this is
                        //  the default.
      apds.setLowThreshold(0); // Sets the low threshold to 0, effectively
                        //  disabling the low side interrupt.
      apds.setHighThreshold(50); // Sets the high threshold to 500. This
                        //  is an arbitrary number I pulled out of thin
                        //  air for purposes of the example. When the CH0
                        //  reading exceeds this level, an interrupt will
                        //  be issued on the INT pin.
      apds.setCyclesForInterrupt(1); // A single reading in the threshold
                        //  range will cause an interrupt to trigger.
      apds.enableInterrupt(APDS9301::INT_ON); // Enable the interrupt.
      apds.clearIntFlag();
      
      
      

    
}

void loop() {
  thing.handle();
  if (isnan(dht.readTemperature())){
      temperature = -1;
  }
  else{
    temperature = dht.readTemperature();
  }
  
  
  
  if (isnan(dht.readHumidity())){
      humiditeAir = -1;
  }
  else{
    humiditeAir = dht.readHumidity();
  }
    
    
    
    

if (analogRead(0)>600){
    humiditeSol = -1;
    
  }
  else{
    humiditeSol = analogRead(0);
  }
    
  
  thing.stream(thing["HumiditeSol"]);
  thing.stream(thing["HumiditeAir"]);
  thing.stream(thing["Luminosite"]);
  thing.stream(thing["Temperature"]);
  
  static unsigned long outLoopTimer = 0;
      apds.clearIntFlag();                          

     
      if (millis() - outLoopTimer >= 1000)
      {
        
        outLoopTimer = millis();
        int value;
        val = analogRead(0); //connect sensor to Analog 0
        Serial.println(value); //print the value to serial port
        Serial.print("Luminous flux: ");
        Serial.println(apds.readCH0Level());
        Serial.println(dht.readHumidity());
        Serial.println(dht.readTemperature());
      };

} 


void lightInt()
    {
      lightIntHappened = true;
    }
