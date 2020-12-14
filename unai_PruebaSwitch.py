import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW) # Salida LED fin de ejercicio
GPIO.setup(24, GPIO.IN) #Entrada fin de carrera

contador = 0

while True:
    inputValue = GPIO.input(24)
    if (inputValue == True):
            contador = contador + 1
            print("Llevas en total ",contador," repeticiones, crack")
            time.sleep(1)
    time.sleep(.01)
    if int(contador) == 3:
            GPIO.output(23, GPIO.HIGH)
            print("Ejercicio finalizado, Espera a que se apague el LED, cabeson")
            contador = 0
            time.sleep(3)
            print("Puedes continuar poniendote cachas, pero no te la vas a coger, salu2")
            GPIO.output(23, GPIO.LOW)

GPIO.cleanup()
        