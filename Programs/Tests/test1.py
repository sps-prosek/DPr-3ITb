import neopixel
from machine import Pin, ADC


def setRgb(color, BRIGHTNESS):
    r, g, b = color
    r = int(r * BRIGHTNESS)
    g = int(g * BRIGHTNESS)
    b = int(b * BRIGHTNESS)
    rgb.fill((r, g, b))
    rgb.write()


rgb = neopixel.NeoPixel(Pin(28), 1)
btnPins = [Pin(20, Pin.IN), Pin(21, Pin.IN), Pin(22, Pin.IN)]
currentStates = [i.value() for i in btnPins]
oldStates = [i.value() for i in btnPins]
adc = ADC(Pin(27))

settings = [255, 255, 255, .5]
rgbState = True
mode = 0
modeMap = {0: "red color", 1: "green color", 2: "blue color", 3: "brightness"}
modeSelected = False

while True:
    currentStates = [i.value() for i in btnPins]
    if not currentStates[0] and oldStates[0]:
        rgbState = not rgbState
        print("RGB led is", "on." if rgbState else "off.")  
    if not currentStates[1] and oldStates[1]:
        mode = mode + 1 if mode < 3 else 0
        modeSelected = False
        print(f"You are on {modeMap[mode]} editing mode. Press button 3 to select.")
    if not currentStates[2] and oldStates[2]:
        modeSelected = True
        print(f"You just selected {modeMap[mode]} editing mode.")
    
    if modeSelected:
        val = adc.read_u16()/65535 if mode == 3 else int(adc.read_u16()*(255/65535))
        settings[mode] = val
    
    if currentStates != oldStates:
        oldStates = [i.value() for i in btnPins]
    
    setRgb(settings[:3], settings[3] if rgbState else .0)
    