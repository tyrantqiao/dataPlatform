# SubscriberTest.py
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe([("gateway/+/rx",0),("application/1/device/+/rx",0)])

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("193.112.44.251", 1883, 60)
client.loop_forever()


