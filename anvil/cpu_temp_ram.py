import anvil.server
from anvil.tables import app_tables
from datetime import datetime
import time
import psutil
anvil.server.connect("PIK2LZE3Z4IB7Y242POIPVRB-Y7UC5RXVIBWVHS3V")

@anvil.server.callable
def ram():
    memory = psutil.virtual_memory()
    memory = memory[1]
    memory = round(memory / 1024 / 1024)
    return(str(memory)+"MB")


while True:
    cpu_percentage = psutil.cpu_percent(interval=1)
    thermal = psutil.sensors_temperatures()
    thermal = round((thermal["cpu_thermal"][0][1]))
    app_tables.pi4server.add_row(
        when=datetime.now(),
        cpu=cpu_percentage,
        temp=thermal
    )
    ram()
    time.sleep(10)

anvil.server.wait_forever()
