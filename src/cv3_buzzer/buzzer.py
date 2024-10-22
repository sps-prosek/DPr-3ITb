from machine import Pin, PWM
from utime import sleep

pin = PWM(Pin(18, Pin.OUT))
btn = Pin(20, Pin.IN)

pin.freq(500)

print("LED starts flashing...")
while True:
    try:
        if btn.value() == 0:
            pin.duty_u16(32768)
        else:
            pin.duty_u16(0)
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")
