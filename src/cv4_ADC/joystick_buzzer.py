from machine import Pin, ADC, PWM
from utime import sleep_ms

buzzer = PWM(Pin(18, Pin.OUT))
x = ADC(Pin(27, Pin.IN))
y = ADC(Pin(26, Pin.IN))

X_LIMITS = (16e3, 5e4)  # 16k to 50k
Y_LIMITS = (16e3, 5e4)  # 16k to 50k
FREQ_LIMITS = (10, 1e4)  # 10 Hz to 10k Hz
DUTY_LIMITS = (0, 32767)  # 0 % to 50 %

print("Start joystick test...")
while True:
    try:
        x_val = x.read_u16()
        y_val = y.read_u16()
        freq = int(
            (x_val - X_LIMITS[0])
            / (X_LIMITS[1] - X_LIMITS[0])
            * (FREQ_LIMITS[1] - FREQ_LIMITS[0])
            + FREQ_LIMITS[0]
        )
        duty = int(
            (y_val - Y_LIMITS[0])
            / (Y_LIMITS[1] - Y_LIMITS[0])
            * (DUTY_LIMITS[1] - DUTY_LIMITS[0])
            + DUTY_LIMITS[0]
        )
        buzzer.freq(freq)
        buzzer.duty_u16(duty)
        sleep_ms(10)
    except KeyboardInterrupt:
        break
buzzer.duty_u16(0)
print("\nFinished.")
