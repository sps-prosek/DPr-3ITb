import neopixel
from machine import Pin
import time
from random import randint, random

rgb = neopixel.NeoPixel(Pin(28), 1)

while True:
    BRIGHTNESS = 1.0  # random()
    r = int(randint(0, 255) * BRIGHTNESS)
    g = int(randint(0, 255) * BRIGHTNESS)
    b = int(randint(0, 255) * BRIGHTNESS)
    rgb.fill((r, g, b))
    rgb.write()
    time.sleep(1)
