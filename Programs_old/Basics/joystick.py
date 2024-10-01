from machine import Pin, ADC
from time import sleep_ms

adcX = ADC(Pin(27))
adcY = ADC(Pin(26))

while True:
    print(f"x: {adcX.read_u16()}, y: {adcY.read_u16()}")
    sleep_ms(100)