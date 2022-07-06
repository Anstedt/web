import anvil.server
from sense_hat import SenseHat

#Uplink app
sense = SenseHat()

@anvil.server.callable
def show_message(message):
    print(message);
    sense.show_message(message);

anvil.server.connect("A4SECVZIGE77VCRMHU7KQKG3-ZMM23X4XTKGC7OGH")

anvil.server.wait_forever()
