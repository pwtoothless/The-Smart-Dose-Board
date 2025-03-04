from hx711 import HX711
import RPi.GPIO as GPIO
hx711 = HX711(
    dout_pin=5,
    pd_sck_pin=6,
    channel='A',
    gain=64
)

hx711.reset()   # Before we start, reset the HX711 (not obligate)
measures = hx711.get_raw_data(num_measures=3)
GPIO.cleanup()  # always do a GPIO cleanup in your scripts!

text = '\n'
print("Weight Measurement:")
for measure in measures:
    text += str(measure) + '\n'
    print(measure)
    print(text)

with open('./weight.txt', 'w') as f:
    f.write(measure)
    f.write(text)
    f.close()

# print("\n".join(measures))