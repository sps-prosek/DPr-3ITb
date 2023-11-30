import neopixel
from machine import Pin, ADC
from time import ticks_ms


def setRgb(color, BRIGHTNESS):
    r, g, b = color
    r = int(r * BRIGHTNESS)
    g = int(g * BRIGHTNESS)
    b = int(b * BRIGHTNESS)
    rgb.fill((r, g, b))
    rgb.write()
    

def callback(pin):
    global btns
    if ticks_ms() - btns[pin]["lastPressTime"] >= 100:
        btns[pin]["lastPressTime"] = ticks_ms()
        btns[pin]["pressed"] = True


rgb = neopixel.NeoPixel(Pin(28), 1)

btnsPins = [Pin(20, Pin.IN), Pin(21, Pin.IN), Pin(22, Pin.IN)]
btns = {
    btnsPins[0]: {"lastPressTime": 0, "pressed": False},
    btnsPins[1]: {"lastPressTime": 0, "pressed": False},
    btnsPins[2]: {"lastPressTime": 0, "pressed": False}
}

for btn in btnsPins:
    btn.irq(trigger=Pin.IRQ_FALLING, handler=callback, hard=True)

adc = ADC(Pin(27))

settings = [255, 255, 255, .5]
rgbState = True
mode = 0
modeMap = {0: "red color", 1: "green color", 2: "blue color", 3: "brightness"}
modeSelected = False

while True:
    if btns[btnsPins[0]]["pressed"]:
        rgbState = not rgbState
        print("RGB led is", "on." if rgbState else "off.")  
        btns[btnsPins[0]]["pressed"] = False
    if btns[btnsPins[1]]["pressed"]:
        mode = mode + 1 if mode < 3 else 0
        modeSelected = False
        print(f"You are on {modeMap[mode]} editing mode. Press button 3 to select.")
        btns[btnsPins[1]]["pressed"] = False
    if btns[btnsPins[2]]["pressed"]:
        modeSelected = True
        print(f"You just selected {modeMap[mode]} editing mode.")
        btns[btnsPins[2]]["pressed"] = False
    
    if modeSelected:
        val = adc.read_u16()/65535 if mode == 3 else int(adc.read_u16()*(255/65535))
        settings[mode] = val
    
    setRgb(settings[:3], settings[3] if rgbState else .0)
    