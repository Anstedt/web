from flask import Flask, jsonify, render_template, request
import paho.mqtt.client as paho
import time

broker="192.168.100.4"
port=1883

sub_topic="clock"

def on_connect(client, userdata, flags, rc):
  # print("Connected with result code "+str(rc))

  # print("subscribing to ",sub_topic)
  client.subscribe(sub_topic)

def on_subscribe(client, userdata, mid, granted_qos):   #create function for callback
  # print("subscribed with qos",granted_qos, "\n")
  pass

def on_message(client, userdata, message):
  m = str(message.payload.decode("utf-8"))
  if m != "Publisher MESSAGE":
    print("message received  ", str(message.payload.decode("utf-8")))

def on_publish(client,userdata,mid):   #create function for callback
  # print("data published mid=",mid, "\n")
  pass

def on_disconnect(client, userdata, rc):
  # print("client disconnected ok")
  pass

#create client object
client= paho.Client("client-socks",transport='tcp')
client.on_connect    = on_connect
client.on_subscribe  = on_subscribe   # assign function to callback
client.on_publish    = on_publish     # assign function to callback
client.on_message    = on_message     # assign function to callback
client.on_disconnect = on_disconnect

print("connecting to broker ",broker,"on port ",port)
client.connect(broker, port)          # establish connection
client.loop_start()                   # Handle messages in the background
# client.publish("clock","From The Web Interface")    # publish example

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

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
