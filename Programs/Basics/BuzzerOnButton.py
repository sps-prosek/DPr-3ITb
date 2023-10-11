from machine import Pin, PWM

buzzer = PWM(Pin(18))
btn = Pin(20, Pin.IN, Pin.PULL_DOWN)

buzzer.freq(500)

while True:
    if not btn.value():
        buzzer.duty_u16(1000)
    else:
        buzzer.duty_u16(0)
