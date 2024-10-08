from machine import Pin
from utime import sleep, ticks_ms

btn20 = Pin(20, Pin.IN)
btn21 = Pin(21, Pin.IN)
btn22 = Pin(22, Pin.IN)

lastBtn20PressTime, lastBtn21PressTime, lastBtn22PressTime = 0, 0, 0
btn20Pressed, btn21Pressed, btn22Pressed = False, False, False


def callback20(pin):
    global lastBtn20PressTime, btn20Pressed
    if ticks_ms() - lastBtn20PressTime >= 100:
        btn20Pressed = True
        lastBtn20PressTime = ticks_ms()


def callback21(pin):
    global lastBtn21PressTime, btn21Pressed
    if ticks_ms() - lastBtn21PressTime >= 100:
        btn21Pressed = True
        lastBtn21PressTime = ticks_ms()


def callback22(pin):
    global lastBtn22PressTime, btn22Pressed
    if ticks_ms() - lastBtn22PressTime >= 100:
        btn22Pressed = True
        lastBtn22PressTime = ticks_ms()


btn20.irq(trigger=Pin.IRQ_FALLING, handler=callback20, hard=True)
btn21.irq(trigger=Pin.IRQ_FALLING, handler=callback21, hard=True)
btn22.irq(trigger=Pin.IRQ_FALLING, handler=callback22, hard=True)

counter = [0, 0, 0]

print("Counter started.")
print("Press Ctrl+C to stop.")
print("Counter value: ", counter)
while True:
    try:
        if btn20Pressed:
            counter[0] += 1
            btn20Pressed = False
            print("Counter value: ", counter)
        if btn21Pressed:
            counter[1] += 1
            btn21Pressed = False
            print("Counter value: ", counter)
        if btn22Pressed:
            counter[2] += 1
            btn22Pressed = False
            print("Counter value: ", counter)
    except KeyboardInterrupt:
        break
print("Finished.")
