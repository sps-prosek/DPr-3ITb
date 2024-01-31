import os
from time import sleep, time
import dht
from machine import Pin

sensor = dht.DHT11(Pin(1))

fileName = "data.txt"

with open(fileName, "w") as f:
    f.write("time, temperature, humidity\n")
    try:
        for i in range(3):
            temp = 0
            hum = 0
            for x in range(3):
                sensor.measure()
                temp += sensor.temperature()
                hum += sensor.humidity()
                sleep(1)
            temp /= 3
            hum /= 3
            data = f"{time()}, {temp}, {hum}"
            print(f"Writing [ {data} ] to file {fileName}")
            f.write(data + "\n")
            sleep(2)
    except OSError:
        pass
print("Done")