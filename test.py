import time
import sys
from hx711 import HX711
import RPi.GPIO as GPIO

DT = 5
SCK = 6

hx = HX711(DT, SCK)
hx.set_reading_format("MSB", "MSB")
hx.tare()

while True:
    try:
        weight = hx.get_weight(5)
        print(f"Weight: {weight} grams")
        time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        GPIO.cleanup()
        sys.exit()