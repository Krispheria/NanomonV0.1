import Jetson.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)

pin_fotorresistor = 18  # Ajustar este número del pin según tu conexión física.
umbral_luz_oscura = 500  # Ajustar según tus necesidades, esto depende de tu ambiente y luz "estándar" que tiene tu habitación.

url_encender_led = 'http://192.168.1.2:80/encender-led'  # Ajustar la URL según la IP de tu módulo (capítulo III-5.3.1)
url_apagar_led = 'http://192.168.1.2:80/apagar-led'  # Ajustar la URL según la IP de tu módulo (capítulo III-5.3.1)

GPIO.setup(pin_fotorresistor, GPIO.IN) # Definir pin del fotorresistor como entrada.

def verificar_luminosidad():
    resistencia_fotorresistor = medir_resistencia_fotorresistor()

    if resistencia_fotorresistor > umbral_luz_oscura:
        encender_led()
    else:
        apagar_led()

def medir_resistencia_fotorresistor(): # Función encargada de medir y obtener la resistencia de la luz con el sensor.
    resistencia_fotorresistor = GPIO.input(pin_fotorresistor)  # Suponiendo que el fotorresistor está en modo pull-up

    return resistencia_fotorresistor

def encender_led(): # Función encargada de encender la luz, ocupa REQUESTS, librería de Python para hacer POST y ocupar HTTP.
    try:
        response = requests.post(url_encender_led)
        response.raise_for_status()
        print('LED encendido')
    except requests.exceptions.RequestException as e:
        print('Error al encender el LED:', e)

def apagar_led():
    try:
        response = requests.post(url_apagar_led)
        response.raise_for_status()
        print('LED apagado')
    except requests.exceptions.RequestException as e:
        print('Error al apagar el LED:', e)

try:
    while True:
        verificar_luminosidad()
        time.sleep(60)

except KeyboardInterrupt:
    GPIO.cleanup()
