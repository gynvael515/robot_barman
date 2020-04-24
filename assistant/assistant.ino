#include <WiFi.h>
#include "Adafruit_MQTT.h"
#include "Adafruit_MQTT_Client.h"
#define WLAN_SSID   "WLAN SSID"
#define WLAN_PASS   "WLAN PASS"
#define AIO_SERVER  "io.adafruit.com"
#define AIO_SERVERPORT  1883
#define AIO_USERNAME     "TU WPISZ NAZWE UZYTKOWNIKA ADAFRUIT"
#define AIO_KEY          "TU WPISZ KEY Z ADAFRUIT"

const int o_PUMP=14;  //powinno działać jako PWM - nie działa
const int o_auxP=13;  //dodatkowe wyjście cyfrowe, sterowane tak jak to PWM
WiFiClient client;
Adafruit_MQTT_Client mqtt(&client, AIO_SERVER, AIO_SERVERPORT, AIO_USERNAME,AIO_KEY);
Adafruit_MQTT_Subscribe pump = Adafruit_MQTT_Subscribe(&mqtt, AIO_USERNAME"/feeds/io-assistant-test");
void MQTT_connect()
{
  //polacz sie z mqtt
    int8_t ret;
    if(mqtt.connected()) return;
    Serial.print("Connecting to MQTT... ");
    uint8_t retries = 3;
    while((ret = mqtt.connect()) != 0)
    {
        Serial.println(mqtt.connectErrorString(ret));
        Serial.println("Retrying MQTT connection in 5 seconds");
        mqtt.disconnect();
        delay(5000);
        retries--;
        if(retries==0)while(true);//dies, wdt resets
    }
    Serial.println("MQTT Connected");
}
void setup()
{   
    //połącz z wifi podanym w definicjach oraz zdefiniuj porty IO płytki(nie działa PWM - nie wiem czemu)
    Serial.begin(115200);
    delay(10);
//    pinMode(o_PUMP,OUTPUT);
    pinMode(o_auxP,OUTPUT);
    ledcSetup(0,100,8);
    ledcAttachPin(o_PUMP,0);
    Serial.println();
    Serial.print("connecting to:");
    Serial.println(WLAN_SSID);
    WiFi.begin(WLAN_SSID,WLAN_PASS);
    while(WiFi.status()!=WL_CONNECTED){
        delay(500);
        Serial.print(".");

    }
    Serial.println("WiFi connected!\nIP address: ");
    Serial.print(WiFi.localIP());
    mqtt.subscribe(&pump);
}

void loop()
{
    MQTT_connect();
    Adafruit_MQTT_Subscribe *subscription;
    while((subscription = mqtt.readSubscription(2000)))
    {
        if (subscription ==&pump)
        {
            Serial.print(F("Got:"));
            Serial.println((char*)pump.lastread);
            if (!strcmp((char*)pump.lastread,"ON"))
//            if((char*)pump.lastread=="ON")
            {
                ledcWrite(o_PUMP,128);
                digitalWrite(o_auxP,HIGH);
            }
            else
            {
                digitalWrite(o_auxP,LOW);
                ledcWrite(o_PUMP,0);
            }
            
        }
    }
}
