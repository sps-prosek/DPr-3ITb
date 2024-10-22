from machine import Pin
from utime import sleep, ticks_ms


class InterruptButton:
    def __init__(self, pin, func):
        self.pin = Pin(pin, Pin.IN)
        self.btnPressed = False
        self.lastBtnPressTime = 0
        self.func = func
        self.pin.irq(trigger=Pin.IRQ_FALLING, handler=self.callback, hard=True)

    def callback(self, pin):
        if ticks_ms() - self.lastBtnPressTime >= 100:
            self.btnPressed = True
            self.lastBtnPressTime = ticks_ms()

    def loop(self):
        if self.btnPressed:
            self.func()
            self.btnPressed = False


def func20():
    global counter
    counter[0] += 1
    print("Counter value: ", counter)


def func21():
    global counter
    counter[1] += 1
    print("Counter value: ", counter)


def func22():
    global counter
    counter[2] += 1
    print("Counter value: ", counter)


btns_array = [
    InterruptButton(20, func20),
    InterruptButton(21, func21),
    InterruptButton(22, func22),
]

counter = [0, 0, 0]

print("Counter started.")
print("Press Ctrl+C to stop.")
print("Counter value: ", counter)
while True:
    try:
        for btn in btns_array:
            btn.loop()
    except KeyboardInterrupt:
        break
print("Finished.")
