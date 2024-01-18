#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include <WiFiClient.h>

/*----------------------CONFIGURACIÓN DE RED Y SEGURIDAD----------------------*/
const char*  WiFi_SSID      = "NOMBRE_DE_LA_RED";
const char*  WiFi_Password  = "CLAVE_DE_LA_RED";
const int    Rele_PIN      = 0; // GPIO00 según datasheet del módulo.
const String Rele_Password = "CLAVE_DE_SEGURIDAD_DE_RELE";
/*-------------CONFIGURACIÓN DE LAS DIRECCIONES Y FUNCIONES--------------------*/

ESP8266WebServer server(80); // Puerto del servidor en el ESP8266

String Estado = "OFF";

void setup(void) {
  pinMode(Rele_PIN, OUTPUT);
  digitalWrite(Rele_PIN, LOW);
  
  Serial.begin(115200); 
  WiFi.begin(WiFi_SSID, WiFi_Password);
  Serial.println("");

  // Esperar hasta tener una conexión exitosa.
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(WiFi_SSID);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP()); // Esta es la Ip local, la cual se debe guardar para el uso posterior.

  if (MDNS.begin("esp8266")) {
    Serial.println("MDNS responder started");
  }

  server.on("/", handleRoot);

  server.begin();
  Serial.println("HTTP server started");
}

void loop(void) {
  server.handleClient();
}

void handleRoot() {
  if (server.method() != HTTP_POST) {
    server.send(405, "text/plain", "Method Not Allowed");
  } else {
    Serial.println(server.arg(0));
    Serial.println(server.arg(1));

    if(server.arg(0) == Rele_Password) {
       if(server.arg(1) == "ON") {
           Estado = "ON";
           server.send(200, "text/plain", Estado);
           digitalWrite(Rele_PIN, HIGH);
       }
       else if(server.arg(1) == "OFF") {
           Estado = "OFF";
           server.send(200, "text/plain", Estado);
           digitalWrite(Rele_PIN, LOW);
       }
       else if(server.arg(1) == "STATE") {
           server.send(200, "text/plain", Estado);
       }
       else {
           server.send(200, "text/plain", "UNKNOWN_COMMAND");
       }
    }
    else {
       server.send(401, "text/plain", "AUTH_FAIL");
    }
  }
}
