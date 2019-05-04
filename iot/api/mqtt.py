import paho.mqtt.client as mqtt
from .models import *
import re
import base64
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    topics=list(Nodes.objects.filter(subscribe=True).values_list('nodeId',flat=True))
    for i,item in enumerate(topics):
        topics[i] = ("application/1/device/"+topics[i]+"/rx",0)
    topics.append(("gateway/+/rx",0))
    print(topics)
    #client.subscribe([("gateway/+/rx",0),("application/1/device/+/rx",0)])
    client.subscribe(topics)
    print("subscribing done")

def on_message(client, userdata, msg):
    str_data=str(msg.payload,encoding="utf-8")
    nodeId = re.search(r'application/1/device/(.*)/rx', msg.topic,re.M|re.I).group(1)
    #data = Data(nodeId=nodeId,)
    json_data=json.loads(str_data)
    print(nodeId+":"+decode_base_data(json_data['data']))
    print(msg.topic+" with  "+ str_data)

def decode_base_data(data):
    hex_data=base64.b64decode(data).hex()
    re_search = re.search('31010001(\d{2}).*0801\d{2}(.*)0901\d{2}(.*)0a03\d{2}(.*)0b03', hex_data,re.M|re.I)
    bool_mode = re_search.group(1)=='01'
    val = re_search.group(2)
    intensity = re_search.group(3)
    time = re_search.group(4)
    print(str(bool_mode)+":"+val+"-----"+intensity+"----------"+time)
    return hex_data

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("193.112.44.251", 1883, 60)
#client.loop_forever()
