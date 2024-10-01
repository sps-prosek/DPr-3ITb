from machine import Pin

btnPins = [Pin(20, Pin.IN), Pin(21, Pin.IN), Pin(22, Pin.IN)]
currentStates = [i.value() for i in btnPins]
oldStates = [i.value() for i in btnPins]
i = [0] * 3

while True:
    currentStates = [i.value() for i in btnPins]
    if not currentStates[0] and oldStates[0]:
        print(f"BTN 1 pressed {i[0]}")
        i[0] += 1
    
    if not currentStates[1] and oldStates[1]:
        print(f"BTN 2 pressed {i[1]}")
        i[1] += 1
    
    if not currentStates[2] and oldStates[2]:
        print(f"BTN 3 pressed {i[2]}")
        i[2] += 1
    
    if currentStates != oldStates:
        oldStates = [i.value() for i in btnPins]