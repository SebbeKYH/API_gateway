# API_gateway

Sebastian Andersson, Rasmus Adolfsson, Ole Lundgren

En sammankoppling av flera oberoende system för att publicera och hämta data från mqtt till api

Embedded system--
ESP32 med temp och luftfuktighets sensorer som publiceras via HiveMQ-topic

MQTT broker--
HiveMQ som tar eomt data som skickas från ESP32

Flask server--
Prenumerar på topic från HiveMQ som görs till json och vidare tillgänglig via API-routes

Apache apisix apigateway--
Hämtar data från flask-serverns API

CLient app--
Hämtar data från apisix gateway och publiceras i clienten
