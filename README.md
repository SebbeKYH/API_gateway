# API_gateway

Sebastian Andersson, Rasmus Adolfsson, Ole Lundgren

Inställningar för APISIX
-----Upstream-----
- Name : weather2
- Host: host.docker.internal
- Port: 9080
-----Route-----
- Name: weather
- Host: host.docker.internal
- Port: 5000
- Path: /*
