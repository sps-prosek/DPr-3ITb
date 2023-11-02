from machine import Pin

btnPin = Pin(20, Pin.IN)
currentState = btnPin.value()
oldState = btnPin.value()
i = 0

while True:
    currentState = btnPin.value()
    if not currentState and oldState:
        print(f"BTN pressed {i}")
        i += 1
    
    if currentState != oldState:
        oldState = btnPin.value()
    