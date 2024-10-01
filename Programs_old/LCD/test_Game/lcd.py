from machine import Pin, I2C, ADC
from utime import sleep_ms, ticks_ms
from grove_lcd_i2c import Grove_LCD_I2C
import random

LCD_SDA = Pin(6)
LCD_SCL = Pin(7)
LCD_ADDR = 62  # 0x3E or 62
i2c = I2C(1, sda=LCD_SDA, scl=LCD_SCL)
print("available i2c devices: ", i2c.scan())
lcd = Grove_LCD_I2C(i2c, LCD_ADDR)

adcX = ADC(Pin(27))
adcY = ADC(Pin(26))

btn1 = Pin(20, Pin.IN, Pin.PULL_UP)
btn2 = Pin(21, Pin.IN, Pin.PULL_UP)
btn3 = Pin(22, Pin.IN, Pin.PULL_UP)

btn1Pressed = False
btn2Pressed = False
btn3Pressed = False

lastBtn1Press = ticks_ms()
lastBtn2Press = ticks_ms()
lastBtn3Press = ticks_ms()


def callbackBtn1(pin):
    global btn1Pressed, lastBtn1Press
    if ticks_ms() - lastBtn1Press >= 100:
        btn1Pressed = True
        lastBtn1Press = ticks_ms()


def callbackBtn2(pin):
    global btn2Pressed, lastBtn2Press
    if ticks_ms() - lastBtn2Press >= 100:
        btn2Pressed = True
        lastBtn2Press = ticks_ms()


def callbackBtn3(pin):
    global btn3Pressed, lastBtn3Press
    if ticks_ms() - lastBtn3Press >= 100:
        btn3Pressed = True
        lastBtn3Press = ticks_ms()


btn1.irq(trigger=Pin.IRQ_FALLING, handler=callbackBtn1)
btn2.irq(trigger=Pin.IRQ_FALLING, handler=callbackBtn2)
btn3.irq(trigger=Pin.IRQ_FALLING, handler=callbackBtn3)


def readJoystick():
    x = (adcX.read_u16() - 32767.5) / 32767.5
    y = -1 * (adcY.read_u16() - 32767.5) / 32767.5

    if -0.2 <= x <= 0.2:
        x = 0.0

    if -0.2 <= y <= 0.2:
        y = 0.0

    return x, y


clamp = lambda n, minn, maxn: max(min(maxn, n), minn)

STEP_PERIOD = 200  # ms

player = "X"
point = "O"

playerPos = [0.0, 0.0]
pointPos = [15, 1]

redraw = True

score = 0

tLastStep = 0

state = 0

gameTime = 20  # seconds
gameStart = ticks_ms()

while True:
    if state == 0:
        if btn1Pressed:
            gameTime -= 5 if gameTime > 5 else 0
            btn1Pressed = False
            redraw = True
        if btn2Pressed:
            state = 1
            gameStart = ticks_ms()
            btn2Pressed = False
            redraw = True
        if btn3Pressed:
            gameTime += 5
            btn1Pressed = btn2Pressed = btn3Pressed = False
            redraw = True
    elif state == 1:
        if ticks_ms() - tLastStep >= STEP_PERIOD:
            x, y = readJoystick()
            playerPos[0] += 2 * x
            playerPos[1] += y
            playerPos[0] = clamp(playerPos[0], 0.0, 15.0)
            playerPos[1] = clamp(playerPos[1], 0.0, 1.0)
            tLastStep = ticks_ms()
            redraw = True
        if ticks_ms() - gameStart >= gameTime * 1000:
            state = 2
            redraw = True
            btn1Pressed = btn2Pressed = btn3Pressed = False
    elif state == 2:
        if btn2Pressed:
            state = 0
            btn1Pressed = btn2Pressed = btn3Pressed = False
            gameTime = 20
            score = 0
            playerPos = [0.0, 0.0]
            pointPos = [15, 1]
            btn2Pressed = False
            redraw = True

    if redraw:
        if state == 0:
            lcd.clear()
            lcd.cursor_position(0, 0)
            lcd.write("Game time:")
            lcd.cursor_position(0, 1)
            lcd.write(str(gameTime) + " s")
        elif state == 1:
            playerX, playerY = int(playerPos[0]), int(playerPos[1])
            pointX, pointY = int(pointPos[0]), int(pointPos[1])

            if playerX == pointX and playerY == pointY:
                score += 1

            while playerX == pointX and playerY == pointY:
                pointPos[0] = random.randint(0, 15)
                pointPos[1] = random.randint(0, 1)
                pointX, pointY = int(pointPos[0]), int(pointPos[1])

            lcd.clear()
            lcd.cursor_position(int(playerPos[0]), int(playerPos[1]))
            lcd.write(player)
            lcd.cursor_position(pointPos[0], pointPos[1])
            lcd.write(point)
        elif state == 2:
            lcd.clear()
            lcd.cursor_position(0, 0)
            lcd.write("Game over!")
            lcd.cursor_position(0, 1)
            lcd.write("Score: " + str(score))
        redraw = False
