from utime import sleep
import network
from machine import reset
import urequests

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
    ip = wlan.ifconfig()
    return ip


def get_time():
    response = urequests.get(
        "https://timeapi.io/api/time/current/zone?timeZone=Europe%2FPrague"
    )
    data = response.json()
    print(data)
    return data["dateTime"]


try:
    ip = connect()
    print(f"Connected to {ssid} on {ip}")
except KeyboardInterrupt:
    reset()


print("LED starts flashing...")
while True:
    try:
        current_time = get_time()
        print(current_time)
        sleep(1)  # sleep 1sec
    except KeyboardInterrupt:
        break
print("Finished.")
