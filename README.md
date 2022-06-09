# iot
If client.loop_start() is called then there is a continuous connect and
disconnect messages. But on_message() works since loop_start() runs a loop() in
the background.

For now default to using loop_start() but does cause logging on the
server. Later we can figure out why this happens.

# Web based code tools and examples
# Flask Call Python Via Ajax
Code in web/flask
- Install Flask
  - pip install flask
  - After creating app.py
- python app.py 
  - Works becasue app.py runs flask
- app.py and templates/json.html allow a button to be created which
  prints hello on the terminal you started app.py
- app.py uses more features and an Ajax method to call python code
- json2.py is a second similar way to call python from buttons but looks a little easier

######################
### Client install ###
######################
- sudo apt-get install mosquitto-clients
$ mosquitto_sub -h "192.168.100.4" -d -t clock
- pip install paho-mqtt

# sudo npm install mqtt
