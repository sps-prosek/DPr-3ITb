from machine import Pin, UART
import time

uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
uart.init(bits=8, parity=0, stop=1)

while True:
    print("sending...")
    uart.write(b"t")
    confirmed = False
    print("waiting for response ")
    while not confirmed:
        print(".", end="")
        if uart.any():
            data = uart.read()
            if data == b"r":
                print("msg confirmed")
                confirmed = True
            else:
                print("wrong data received")
        time.sleep(0.2)
    time.sleep(1)
