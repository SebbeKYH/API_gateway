import json
from flask import Flask, Response
import paho.mqtt.client as paho

def create_app():
    app = Flask(__name__)

    app.config['MQTTBROKER'] = {
        'URL': 'broker.mqttdashboard.com',
        'port': 1883,
        'username': 'ROS',
        'password': 'ROS1',
        'topic': '/weather/ROS'
    }

    @app.route("/weather_api/v1/temp", methods=['GET'])
    def get_temp():
        return Response(json.dumps(json_message['temp']), 200, content_type='application/json')

    @app.route("/weather_api/v1/humidity", methods=['GET'])
    def get_humidity():
        return Response(json.dumps(json_message['humidity']), 200, content_type='application/json')

    @app.route("/weather_api/v1/", methods=['GET'])
    def get_all_weather():
        return Response(json.dumps(json_message), 200, content_type='application/json')

    return app


def on_subscribe(var1, var2, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))


def on_connect(rc):
    print('CONNACK received with code %d.' % rc)


def on_message(client, userdata, msg):
    global message
    global json_message
    message =str(msg.payload.decode("utf-8"))
    json_message = json.loads(message)

client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect('broker.mqttdashboard.com', 1883)
client.subscribe('/weather/ROS', qos=1)

client.loop_start()

if __name__ == '__main__':
    app = create_app()
    app.run()