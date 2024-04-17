from machine import Pin, UART

RESPONSE_TIMEOUT_MS = 500
DATA_PATCH_SIZE = 10

uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
uart.init(bits=8, parity=0, stop=1, timeout=RESPONSE_TIMEOUT_MS)

fName = "text.txt"


def sendFileName():
    fNameBytes = fName.encode("utf-8")
    toSend = (
        (1).to_bytes(1, "little") + len(fNameBytes).to_bytes(1, "little") + fNameBytes
    )
    passed = False
    while not passed:
        print("Sending msg: ", toSend)
        uart.write(toSend)
        ret = uart.read(1)
        print("Received msg: ", ret)
        if ret == b"\x01":
            passed = True
            print("File name sended")


def sendFileData():
    i = 0
    with open(fName, "rb") as f:
        finished = False
        while not finished:
            data = f.read(DATA_PATCH_SIZE)
            if len(data) == 0:
                finished = True
                break
            toSend = (2).to_bytes(1, "little") + len(data).to_bytes(1, "little") + data
            passed = False
            while not passed:
                print("Sending msg: ", toSend)
                uart.write(toSend)
                ret = uart.read(1)
                print("Received msg: ", ret)
                if ret == b"\x02":
                    passed = True
                    print("Batch ", i, " sended")
                    i += 1


def end():
    toSend = (3).to_bytes(1, "little")
    passed = False
    while not passed:
        print("Sending msg: ", toSend)
        uart.write(toSend)
        ret = uart.read(1)
        print("Received msg: ", ret)
        if ret == b"\x03":
            passed = True
            print("End command sended")


sendFileName()
sendFileData()
end()
