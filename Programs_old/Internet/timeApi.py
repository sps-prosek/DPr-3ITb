import network
from time import sleep
import machine
import urequests

ssid = "SPS-PROSEK HOST"
password = ""

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print(f"Connection to {ssid}...")
        sleep(1)
    ip = wlan.ifconfig()[0]
    return ip

try:
    ip = connect()
    print(f"Connected to {ssid} with ip {ip}")
except KeyboardInterrupt:
    machine.reset()


def get_time():
    response = urequests.get("http://worldtimeapi.org/api/timezone/Europe/Prague")
    data = response.json()
    print(data)
    return data["datetime"]

current_time = get_time()
print(current_time)