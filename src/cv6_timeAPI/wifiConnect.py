from utime import sleep
import network

ssid = "SPS-PROSEK HOST"
password = ""


def connect():
    # Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print("Waiting for connection...")
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f"Connected on {ip}")
    return ip


print("LED starts flashing...")
while True:
    try:
        ip = connect()
        sleep(1)  # sleep 1sec
    except KeyboardInterrupt:
        break
print("Finished.")
