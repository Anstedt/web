from flask import Flask, jsonify, render_template, request
import paho.mqtt.client as paho
import time

broker="192.168.100.4"
port=1883

sub_topic="clock"

def on_subscribe(client, userdata, mid, granted_qos):   #create function for callback
  print("subscribed with qos",granted_qos, "\n")
  pass

def on_message(client, userdata, message):
  global duration
  global running
  m = str(message.payload.decode("utf-8"))
  print("message received  ", str(message.payload.decode("utf-8")))

def on_publish(client,userdata,mid):   #create function for callback
  print("data published mid=",mid, "\n")
  pass

def on_disconnect(client, userdata, rc):
  print("client disconnected ok")

client= paho.Client("client-socks",transport='tcp')       #create client object
client.on_subscribe = on_subscribe       #assign function to callback
client.on_publish = on_publish        #assign function to callback
client.on_message = on_message        #assign function to callback
client.on_disconnect = on_disconnect
print("connecting to broker ",broker,"on port ",port)
client.connect(broker,port)           #establish connection
client.loop_start()
print("subscribing to ",sub_topic)
client.subscribe(sub_topic)
client.publish("clock","From The Web")    #publish

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ButtonOne')
def ButtonOne():
    print('Printed From ONE')
    client.publish("clock","Web Button ONE")
    return "Nothing"

@app.route('/ButtonTwo')
def ButtonTwo():
  print('Printed From TWO')
  client.publish("clock","Web Button TWO")
  return "Nothing"

#Keep the program running and print out the date time
#while True:
#  time.sleep(1)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
