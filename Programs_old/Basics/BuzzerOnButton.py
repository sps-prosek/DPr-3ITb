from machine import Pin, PWM

buzzer = PWM(Pin(18))
btn = Pin(20, Pin.IN)

buzzer.freq(500)

while True:
    buzzer.duty_u16(0 if btn.value() else 1000)
