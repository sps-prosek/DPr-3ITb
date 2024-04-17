from machine import Pin, UART

uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
uart.init(bits=8, parity=0, stop=1)

f = None

while True:
    if uart.any():
        msg = uart.read()
        print("msg: " + str(msg))
        if msg[0] == 1:
            fName = msg[2 : msg[1] + 2].decode()
            print(f"Opening file {fName}")
            f = open(fName, "wb")
            uart.write(b"\x01")
        elif msg[0] == 2:
            print("receiving data")
            if f != None:
                f.write(msg[2 : msg[1] + 2])
                print(f"Received {msg[1]} bytes")
                uart.write(b"\x02")
        elif msg[0] == 3:
            if f != None:
                f.close()
                uart.write(b"\x03")
                print("file received")
