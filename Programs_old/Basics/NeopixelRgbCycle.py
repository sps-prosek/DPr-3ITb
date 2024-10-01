import neopixel
from machine import Pin
import time

rgb = neopixel.NeoPixel(Pin(28), 1)  # pin and number of LEDs in strip

BRIGHTNESS = 0.5


def setBrightness(color):
    r, g, b = color
    r = int(r * BRIGHTNESS)
    g = int(g * BRIGHTNESS)
    b = int(b * BRIGHTNESS)
    return (r, g, b)


while True:
    rgb.fill(setBrightness((255, 0, 0)))
    rgb.write()
    time.sleep(1)
    rgb.fill(setBrightness((0, 255, 0)))
    rgb.write()
    time.sleep(1)
    rgb.fill(setBrightness((0, 0, 255)))
    rgb.write()
    time.sleep(1)
    rgb.fill(setBrightness((0, 0, 0)))
    rgb.write()
    time.sleep(1)
