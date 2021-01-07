import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
import paho.mqtt.publish as publish
import json 

MQTT_SERVER = "169.254.189.170"
MQTT_PATH = "test_channel"

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW) # Salida LED fin de ejercicio
GPIO.setup(24, GPIO.IN) #Entrada fin de carrera

reader = SimpleMFRC522()

lista_usuarios = [{'id': 796415616291,'Nombre': 'Contrasta','Repeticiones' : 12},
                  {'id': 800003948682,'Nombre': 'Jorge','Repeticiones' : 10},
                  {'id': 1002848969990,'Nombre': 'Gibello','Repeticiones' : 6},
                  {'id': 649130914353,'Nombre': 'Arjona','Repeticiones' : 8}]

def buscarUsuario(usuario):
    for item in lista_usuarios:
        if item['id'] == usuario:
            usuarioEncontrado = item
            break
    return usuarioEncontrado    
    

def verRepeticiones(id):
    user = buscarUsuario(id)
    print("Bienvenido", user['Nombre'])
    print("Te faltan "+str(user['Rep")
eticiones'])+" repeticiones")
    repes = user['Repeticiones']
    while repes != 0:         
        inputValue = GPIO.input(24)
        if (inputValue == True):
            repes = repes -1
            print("Te faltan "+str(repes)+" repeticiones")
            time.sleep(1)
            if repes == 0:
                GPIO.output(23, GPIO.HIGH)
                print("Ejercicio finalizado, Espera a que se apague el LED")
                time.sleep(3)
                print("Puedes continuar poniendote cachas, salu2")
                user_json= json.dumps(user)
                publish.single(MQTT_PATH, user_json, hostname=MQTT_SERVER)
                GPIO.output(23, GPIO.LOW)

try:
    print("Acerca la tarjeta")
    id,text = reader.read()
    verRepeticiones(id)


finally:
        GPIO.cleanup()