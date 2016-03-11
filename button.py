import requests
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

button_pin = 25
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(button_pin)
    if input_state == False:
        print('Button Pressed')
        r = requests.post('http://textbelt.com/text', data = {'number':'', 'message':'the mail is here.'})
        time.sleep(0.5)

