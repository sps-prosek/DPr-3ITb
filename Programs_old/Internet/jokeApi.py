import network
from time import sleep, localtime
import machine
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
    ip = wlan.ifconfig()[0]
    print(f"Connected on {ip}")
    return ip


try:
    ip = connect()
except KeyboardInterrupt:
    machine.reset()


def get_joke():
    response = urequests.get("https://v2.jokeapi.dev/joke/Any")
    data = response.json()
    #print(data)
    ret = None
    if data["type"] == "single":
        ret = str(data["joke"])
    elif data["type"] == "twopart":
        ret = str(data["setup"]) + "\n" + str(data["delivery"])
    return ret

while True:
    joke = get_joke()
    print(joke, end="\n\n\n")
    sleep(10)
