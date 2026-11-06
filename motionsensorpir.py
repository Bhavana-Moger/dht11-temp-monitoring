import RPi.GPIO as GPIO
import time

PIR = 17
BUZZER = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)

try:
    while True:
        if GPIO.input(PIR):
            print("Motion Detected!")
            GPIO.output(BUZZER, GPIO.HIGH)
        else:
            print("No Motion")
            GPIO.output(BUZZER, GPIO.LOW)

        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
