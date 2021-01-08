import paho.mqtt.client as mqtt
import json
 
MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe(MQTT_PATH)
    

 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    usuario = msg.payload.decode('utf-8')
    usuario_json =json.loads(usuario)
    print("El usuario",usuario_json['Nombre'],"ha terminado sus",usuario_json['Repeticiones'],"repeticiones.")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)
client.loop_forever()
