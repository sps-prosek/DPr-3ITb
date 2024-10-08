from machine import Pin
from utime import sleep, ticks_ms


class InterruptButton:
    def __init__(self, pin):
        self.pin = Pin(pin, Pin.IN)
        self.btnPressed = False
        self.lastBtnPressTime = 0
        self.pin.irq(trigger=Pin.IRQ_FALLING, handler=self.callback, hard=True)

    def callback(self, pin):
        if ticks_ms() - self.lastBtnPressTime >= 100:
            self.btnPressed = True
            self.lastBtnPressTime = ticks_ms()

    def isPressed(self):
        return self.btnPressed

    def reset(self):
        self.btnPressed = False


btn20 = InterruptButton(20)
btn21 = InterruptButton(21)
btn22 = InterruptButton(22)

counter = [0, 0, 0]

print("Counter started.")
print("Press Ctrl+C to stop.")
print("Counter value: ", counter)
while True:
    try:
        if btn20.isPressed():
            counter[0] += 1
            btn20.reset()
            print("Counter value: ", counter)
        if btn21.isPressed():
            counter[1] += 1
            btn21.reset()
            print("Counter value: ", counter)
        if btn22.isPressed():
            counter[2] += 1
            btn22.reset()
            print("Counter value: ", counter)
    except KeyboardInterrupt:
        break
print("Finished.")
