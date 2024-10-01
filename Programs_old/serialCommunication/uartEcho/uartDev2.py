from machine import Pin, UART
import time

uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
uart.init(bits=8, parity=0, stop=1)

while True:
    if uart.any():
        data = uart.read()
        if data == b"t":
            uart.write(b"r")
    time.sleep(1)
