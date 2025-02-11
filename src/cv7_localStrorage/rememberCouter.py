from machine import Pin
from utime import ticks_ms
import json

F_NAME = "config.json"


class JsonFile:
    def __init__(self, fname) -> None:
        self.fname = fname

    def read(self):
        try:
            with open(self.fname, "r") as f:
                ret = json.load(f)
        except OSError:
            ret = {}
        return ret

    def write(self, data):
        with open(self.fname, "w") as f:
            f.write(json.dumps(data))


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


btn = InterruptButton(20)
config = JsonFile("config.json")

data = config.read()
if "x" in data:
    x = data["x"]
else:
    x = 0


print("Counter started.")
print("Press Ctrl+C to stop.")
print("Counter value: ", x)
while True:
    try:
        if btn.btnPressed:
            x += 1
            config.write({"x": x})
            print(x)
            btn.btnPressed = False
    except KeyboardInterrupt:
        break
print("Finished.")
