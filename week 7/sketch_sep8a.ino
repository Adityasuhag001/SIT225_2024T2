

#include <DHT.h>
#define DHTPIN 2       // I wired DATA to digital pin 2
#define DHTTYPE DHT22  // we are using DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
  // Print a small header once so I remember the column order when logging
  Serial.println("# temperature_c,humidity_pct");
  delay(1000);
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature(); // in °C by default

  // If sensor read fails, skip this loop and try again
  if (isnan(h) || isnan(t)) {
    // I print a comment line so my logger can ignore it if needed
    Serial.println("# read failed");
  } else {
    // I only print 2 numbers separated by comma for easy CSV logging
    Serial.print(t, 2); Serial.print(",");
    Serial.println(h, 2);
  }
  delay(2000); // every ~2s 
}


