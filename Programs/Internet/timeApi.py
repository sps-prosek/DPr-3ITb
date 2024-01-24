import network
from time import sleep, localtime
import machine
import urequests

ssid = "SSID"
password = "PASSWORD"


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


try:
    ip = connect()
except KeyboardInterrupt:
    machine.reset()


def get_time():
    response = urequests.get("http://worldtimeapi.org/api/timezone/Europe/Prague")
    data = response.json()
    print(data)
    timestamp = data["unixtime"]
    return timestamp


current_time = get_time()
print(current_time)
formatted_time = localtime(current_time)
print(formatted_time)
