from machine import Pin, PWM

led = Pin(0, Pin.OUT)
btn = Pin(20, Pin.IN)

while True:
    led.value(not btn.value())
