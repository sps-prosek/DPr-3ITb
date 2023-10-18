from machine import Pin
from time import ticks_ms, sleep
from random import randrange


btn = Pin(8, Pin.IN)
led = Pin(9, Pin.OUT)

led.off()

while True:
    sleepT = randrange(2, 10)
    sleep(sleepT)
    led.on()
    t0 = ticks_ms()
    olfBtn = btn.value()
    while btn.value() == olfBtn:
        continue
    print(f"{ticks_ms() - t0} ms")
    led.off()
    