// SIT225 - LED Blink Protocol (simple)
const int LED_PIN = 13;

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  randomSeed(analogRead(A0)); // harmless if A0 floating
}

void loop() {
  if (Serial.available() > 0) {
    int n = Serial.parseInt();      // number from Python
    if (n <= 0) { while (Serial.available()) Serial.read(); return; }

    // Blink n times (0.5s on/off)
    for (int i = 0; i < n; i++) {
      digitalWrite(LED_PIN, HIGH); delay(500);
      digitalWrite(LED_PIN, LOW);  delay(500);
    }

    // Send a random wait time (2..6) back to Python
    int waitTime = random(2, 7);    // upper bound exclusive
    Serial.println(waitTime);
  }
}

