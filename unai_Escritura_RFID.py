import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import sys
sys.path.append('/home/pi/MFRC522-python')

reader = SimpleMFRC522()

try:
        text = input('New data:')
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
finally:
        GPIO.cleanup()