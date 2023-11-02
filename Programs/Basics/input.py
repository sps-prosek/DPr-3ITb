from machine import Pin, PWM

buzzer = PWM(Pin(18))

freq = 500
buzOn = False
duty = 1000

buzzer.freq(freq)
buzzer.duty_u16(1000 if buzOn else 0)

while True:
    comm = input()
    if comm == "ON":
        buzOn = True
    elif comm == "OFF":
        buzOn = False
    else:
            
        try:
            if comm[:2] == "f ":
                freq = int(comm[2:])
            elif comm[:2] == "d ":
                duty = int(comm[2:])
        except:
            print("Command error")
    buzzer.freq(freq)
    buzzer.duty_u16(duty if buzOn else 0)