
import speedtest 
import paho.mqtt.client as mqtt
 
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    #client.subscribe("CoreElectronics/test")
    #client.subscribe("CoreElectronics/topic")



st = speedtest.Speedtest() 


print('Download speed')
print(st.download())
print('Upload speed')
print(st.upload()) 
servernames =[] 
st.get_servers(servernames) 
print('Ping')
print(st.results.ping) 


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    if msg.payload == "Hello":
        print("Received a message from the server")

    if msg.payload == "World!":
        print("another messsage received")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("test.mosquitto.org", 1883, 60)
 
client.loop_forever()