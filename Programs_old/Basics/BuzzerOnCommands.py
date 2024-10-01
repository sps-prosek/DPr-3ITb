from machine import Pin, PWM

def setBuzzer():
    buzzer.freq(freq)
    buzzer.duty_u16(duty if buzzOn else 0)

buzzer = PWM(Pin(18))

freq = 500
duty = 500
buzzOn = False

while True:
    comm = input("Enter command: ").lower().split(":")
    if comm[0] == "on":
        buzzOn = True
    elif comm[0] == "off":
        buzzOn = False
    elif comm[0] == "set":
        try:
            if comm[1] == "freq":
                freq = int(comm[2])
            elif comm[1] == "duty":
                duty = int(comm[2])
        except:
            print("Wrong command format !!!")
    else:
        print("Unknown command ...")
    setBuzzer()
        
