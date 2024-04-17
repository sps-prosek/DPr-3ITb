from machine import *
from utime import sleep
from grove_lcd_i2c import Grove_LCD_I2C

LCD_SDA = Pin(8)
LCD_SCL = Pin(9)
LCD_ADDR = 62  # 0x3E or 62
i2c = I2C(0, sda=LCD_SDA, scl=LCD_SCL)
print("available i2c devices: ", i2c.scan())
lcd = Grove_LCD_I2C(i2c, LCD_ADDR)

lcd.home()
lcd.write("Raspberry Pi\nPico")

sleep(3)

lcd.clear()
lcd.write("Idx:")

i = 0

while True:
    i += 1
    lcd.cursor_position(5, 0)
    lcd.write(str(i))
    sleep(1)
