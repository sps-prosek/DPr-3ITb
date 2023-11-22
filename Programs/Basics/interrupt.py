from machine import Pin
from time import ticks_ms

btnPressed = False
lastBtnPress = ticks_ms()
btn = Pin(2, Pin.IN, Pin.PULL_UP)
n = 0

def callback(pin):
    global btnPressed, lastBtnPress
    if ticks_ms() - lastBtnPress >= 100:
        btnPressed = True
        lastBtnPress = ticks_ms()

btn.irq(trigger=Pin.IRQ_FALLING, handler=callback, hard=True)

while True:
    if btnPressed:
        print(f"Button was pressed {n}")
        n += 1
        btnPressed = False