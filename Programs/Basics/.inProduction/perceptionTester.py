from machine import Pin
from random import randrange
from time import sleep, ticks_ms

btn = Pin(8, Pin.IN)
led = Pin(9, Pin.OUT)

led.off()

while True:
    sleepT = randrange(2, 10)
    sleep(sleepT)
    led.on()
    t0 = ticks_ms()
    while btn.value():
        continue
    print(ticks_ms() - t0)
    led.off()
