  #!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
sys.path.append('/home/pi/MFRC522-python')
from mfrc522 import SimpleMFRC522


reader = SimpleMFRC522()
while True:
    print("Acerca tu tarjeta de socio")

    try:
        id, text = reader.read()
        print(id)
        print("Bienvenido: ",text)

    finally:
        GPIO.cleanup()