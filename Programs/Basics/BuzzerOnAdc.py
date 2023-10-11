from machine import Pin, PWM, ADC

buzzer = PWM(Pin(18))
btn = Pin(20, Pin.IN, Pin.PULL_DOWN)
adc = ADC(Pin(27))  # adc only on pins 26, 27, 28

buzzer.freq(500)

while True:
    if not btn.value():
        # When button is pressed read adc pin and set buzzer duty
        buzzer.duty_u16(adc.read_u16())
        print(adc.read_u16())
    else:
        buzzer.duty_u16(0)
