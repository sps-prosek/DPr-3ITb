from machine import Pin, ADC
from utime import sleep

x = ADC(Pin(27, Pin.IN))
y = ADC(Pin(26, Pin.IN))

print("Start joystick test...")
while True:
    try:
        print("\rX: ", x.read_u16(), "Y: ", y.read_u16(), end="")
        sleep(0.1)
    except KeyboardInterrupt:
        break
print("\nFinished.")
