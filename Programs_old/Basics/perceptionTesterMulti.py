from machine import Pin
from time import ticks_ms, sleep
from random import randrange

class Player:
    def __init__(self, btnPin, ledPin, name) -> None:
        self.__btnPin = Pin(btnPin)
        self.__ledPin = Pin(ledPin, Pin.OUT)
        self.__name = name
        self.__t0 = 0
        self.__duration = 0
        
        self.__btnPin.irq(self.__callback, Pin.IRQ_FALLING)
    
    def set(self, t0):
        self.__ledPin.on()
        self.__t0 = t0
    
    def __callback(self, pin):
        self.__duration = ticks_ms() - self.__t0
        self.__ledPin.off()

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
    