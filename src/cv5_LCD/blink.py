from machine import Pin, I2C
from utime import sleep, ticks_ms, sleep_ms
from grove_lcd_i2c import Grove_LCD_I2C


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


SDA_PIN = Pin(8)
SCL_PIN = Pin(9)
i2c = I2C(0, sda=SDA_PIN, scl=SCL_PIN)
I2C_ADDR = 62  # 0x3e

lcd = Grove_LCD_I2C(i2c, I2C_ADDR)

right = InterruptButton(20)
left = InterruptButton(21)
down = InterruptButton(22)

lcd.clear()
lcd.home()
lcd.write("Hello, World!")

sleep(3)  # sleep 3sec

lcd.clear()

x, y = 0, 0

print("LED starts flashing...")
while True:
    try:
        if right.btnPressed:
            x = (x + 1) % 16
            right.btnPressed = False
        if left.btnPressed:
            x = (x - 1) % 16
            left.btnPressed = False
        if down.btnPressed:
            y = (y + 1) % 2
            down.btnPressed = False
        lcd.clear()
        lcd.cursor_position(x, y)
        lcd.write("X")
        sleep_ms(100)
    except KeyboardInterrupt:
        break
print("Finished.")
