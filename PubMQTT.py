  #!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
sys.path.append('/home/pi/MFRC522-python')
from mfrc522 import SimpleMFRC522
import paho.mqtt.publish as publish
import json

topic = "txuatxe/rpi1"
hostname = "test.mosquitto.org"
mensaje = {}

reader = SimpleMFRC522()
id, text = reader.read()
idString = str(id)

usuario1 = {'Nombre':"Aitor",
            'Apellido' : "Constrasta",
            'Edad' : "21",
            'series': 3,
            'repeticiones': 10}

usuario2 = {'Nombre':'Jorge',
            'Apellido' : 'Lodoso',
            'Edad' : 21,
            'series': 5,
            'repeticiones': 5}

usuario3 = {'Nombre':'Unai',
            'Apellido' : 'Gibello',
            'Edad' : 29,
            'series': 4,
            'repeticiones': 12}

usuario4 = {'Nombre':'Laura',
            'Apellido' : 'Apruebanos',
            'Edad' : 31,
            'series': 5,
            'repeticiones': 6}


while True:
    try:    
       
        if idString[0] == "1":
            mensaje = usuario1
                    
        elif idString[0] == "7":
            mensaje = usuario2
            
        elif idString[0] == "8":
            mensaje = usuario3
            
        elif idString[0] == "6":
            mensaje = usuario4
            
        mensaje_json= json.dumps(mensaje)
        publish.single("txuatxe/rpi1", mensaje_json, hostname=hostname)
        print("El usuaario es: ",mensaje_json)
        
    finally:
        GPIO.cleanup()
        

        
        
        
    