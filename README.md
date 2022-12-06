# API_gateway

Sebastian Andersson, Rasmus Adolfsson, Ole Lundgren

Inställningar för APISIX
__Upstream__
- Name : weather2
- Host: host.docker.internal
- Port: 9080
__Route__
- Name: weather
- Host: host.docker.internal
- Port: 5000
- Path: /*
