from machine import Pin
from utime import sleep

btnPin = Pin(20, Pin.IN)
lastBtnState = btnPin.value()
currentBtnState = btnPin.value()

x = 0

print("Counter started.")
print("Press Ctrl+C to stop.")
print("Counter value: ", x)
while True:
    try:
        currentBtnState = btnPin.value()
        if lastBtnState == 1 and currentBtnState == 0:
            x += 1
            print("Counter value: ", x)
        lastBtnState = currentBtnState
    except KeyboardInterrupt:
        break
print("Finished.")
