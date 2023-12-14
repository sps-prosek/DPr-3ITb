from machine import Pin
from time import ticks_ms


def callback(pin):
    global btnData
    if ticks_ms() - btnData[pin]["lastPress"] >= 100:
        btnData[pin]["pressed"] = True
        btnData[pin]["lastPress"] = ticks_ms()


def printPeriod():
    global period
    print(f"Period updated: period = {period} s")


btnPlus = Pin(20, Pin.IN)
btnMinus = Pin(21, Pin.IN)
btnData = {
    btnPlus: {
        "lastPress": 0,
        "pressed": False
    },
    btnMinus: {
        "lastPress": 0,
        "pressed": False
    }
}
btnPlus.irq(trigger=Pin.IRQ_FALLING, handler=callback, hard=True)
btnMinus.irq(trigger=Pin.IRQ_FALLING, handler=callback, hard=True)

ledGreen = Pin(5, Pin.OUT)
ledYellow = Pin(3, Pin.OUT)
ledRed = Pin(1, Pin.OUT)

period = 0.5 #s
STEP = 0.1
PERIOD_LIMIT = 0.1

state = 0
lastStepUpdate = 0

ledStates = {
    0: [ledGreen.off, ledYellow.off, ledRed.on],
    1: [ledGreen.off, ledYellow.on, ledRed.on],
    2: [ledGreen.on, ledYellow.off, ledRed.off],
    3: [ledGreen.off, ledYellow.on, ledRed.off]
}

while True:
    if btnData[btnPlus]["pressed"]:
        period = period + STEP
        printPeriod()
        btnData[btnPlus]["pressed"] = False
    
    if btnData[btnMinus]["pressed"]:
        period = period - STEP if period >= PERIOD_LIMIT + STEP else PERIOD_LIMIT
        printPeriod()
        btnData[btnMinus]["pressed"] = False
    
    if ticks_ms() - lastStepUpdate >= period * 1000:
        state = state + 1 if state < 3 else 0
        lastStepUpdate = ticks_ms()
        for i in ledStates[state]: i()