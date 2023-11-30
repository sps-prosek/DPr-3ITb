import neopixel
from machine import Pin, ADC
from time import ticks_ms

class MyPin(Pin):
    def __init__(self, id: int | str, mode: int = Pin.IN, pull: int = Pin.PULL_UP):
        super().__init__(id, mode, pull)
        self.__t0 = 0
        self.__pressed = False
    
    def timeFromLastPress(self):
        return ticks_ms() - self.__t0
    
    def press(self):
        self.__pressed = True
        self.__t0 = ticks_ms()
    
    def unPress(self):
        self.__pressed = False
    
    def pressed(self):
        return self.__pressed
    


def setRgb(color, BRIGHTNESS):
    r, g, b = color
    r = int(r * BRIGHTNESS)
    g = int(g * BRIGHTNESS)
    b = int(b * BRIGHTNESS)
    rgb.fill((r, g, b))
    rgb.write()


def callback(pin):
    if pin.timeFromLastPress() >= 100:
        pin.press()


rgb = neopixel.NeoPixel(Pin(28), 1)
btns = [MyPin(20, Pin.IN), MyPin(21, Pin.IN), MyPin(22, Pin.IN)]

btns[0].irq(trigger=Pin.IRQ_FALLING, handler=lambda pin: callback(btns[0]), hard=True)
btns[1].irq(trigger=Pin.IRQ_FALLING, handler=lambda pin: callback(btns[1]), hard=True)
btns[2].irq(trigger=Pin.IRQ_FALLING, handler=lambda pin: callback(btns[2]), hard=True)

adc = ADC(Pin(27))

settings = [255, 255, 255, .5]
rgbState = True
mode = 0
modeMap = {0: "red color", 1: "green color", 2: "blue color", 3: "brightness"}
modeSelected = False

while True:
    if btns[0].pressed():
        rgbState = not rgbState
        print("RGB led is", "on." if rgbState else "off.")  
        btns[0].unPress()
    if btns[1].pressed():
        mode = mode + 1 if mode < 3 else 0
        modeSelected = False
        print(f"You are on {modeMap[mode]} editing mode. Press button 3 to select.")
        btns[1].unPress()
    if btns[2].pressed():
        modeSelected = True
        print(f"You just selected {modeMap[mode]} editing mode.")
        btns[2].unPress()
    
    if modeSelected:
        val = adc.read_u16()/65535 if mode == 3 else int(adc.read_u16()*(255/65535))
        settings[mode] = val
    
    setRgb(settings[:3], settings[3] if rgbState else .0)
    