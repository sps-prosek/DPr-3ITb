from machine import Pin, ADC, PWM
from utime import sleep

led = PWM(Pin(9, Pin.OUT))
adc = ADC(Pin(27, Pin.IN))

led.freq(10000)

print("Start ADC test...")
while True:
    try:
        led.duty_u16(adc.read_u16())
    except KeyboardInterrupt:
        break
led.duty_u16(0)
print("Finished.")
