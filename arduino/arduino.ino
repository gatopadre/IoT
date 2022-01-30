#include <DHT.h>


/* contants */
#define baudrate              9600 // resfresh rate of arduino
#define action_off            "0" // off led builtin 
#define action_on             "1" // on led builtin
#define action_read_temp      "2" // read temperature sensor dht
#define action_read_hum       "3" // read temperature sensor dht
#define action_read_lum       "4" // read temperature sensor dht

/* pin sets */
#define dht_pin               5 // pin del sensor de temperatura y humedad
#define led_builtin_pin       LED_BUILTIN // led builtin pin
#define ldr_pin               A0

/* OBJECTS */
#define dhttype               DHT11 // tipo del modulo de temperatura y humedad
DHT dht(dht_pin, dhttype);    // instanciando el modulo de temperatura y humedad

float temperature = -1; // temperature var
float humidity = -1; // humidity var
float luminocity = -1; // luminocity var

/* configurations */
void setup() {
    Serial.begin(baudrate);
    while (!Serial) {
      ; // wait for serial port to connect. Needed for native USB port only
    }
    pinMode(led_builtin_pin, OUTPUT); 
    pinMode(dht_pin, INPUT);
    pinMode(ldr_pin, INPUT);
    dht.begin(); //Se inicia el sensor
}

void loop() {
  if (Serial.available() > 0) {
      String action = Serial.readStringUntil('\n');   
      if (action.equals(action_on)) {
        digitalWrite(led_builtin_pin, HIGH);     
        parseResponse("Turn on Led Builtin");
      } else if (action.equals(action_off)) {
        digitalWrite(led_builtin_pin, LOW);
        parseResponse ("Turn off Led Builtin");
      } else if (action.equals(action_read_temp)) {
        temperature = dht.readTemperature();
        parseResponse (String(temperature));
        temperature = -1;
      } else if (action.equals(action_read_hum)) {
        humidity = dht.readHumidity();
        parseResponse (String(humidity));
        humidity = -1;
      } else if (action.equals(action_read_lum)) {
        luminocity = digitalRead(ldr_pin);
        // luminocity = analogRead(ldr_pin);
        parseResponse (String(luminocity));
        luminocity = -1;
      } else {
        parseResponse("Uknow order received");
      }
  }
}

/* functions */
void parseResponse (String action){
    Serial.println("" + action + "\n");
}
