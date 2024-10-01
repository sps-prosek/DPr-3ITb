import os
from time import sleep_ms, time
import dht
from machine import Pin
import json

sensor = dht.DHT11(Pin(1))

with open("config.json", "r") as cf:
    cnf = json.load(cf)

with open(cnf["file name"], "w") as f:
    f.write(f"{cnf['sensor name']}\ntime, temperature, humidity\n")
    try:
        for i in range(cnf["cycles"]):
            temp = 0
            hum = 0
            for x in range(cnf["mean"]["samples"]):
                sensor.measure()
                temp += sensor.temperature()
                hum += sensor.humidity()
                sleep_ms(cnf["mean"]["period ms"])
            temp /= cnf["mean"]["samples"]
            hum /= cnf["mean"]["samples"]
            data = f"{time()}, {temp}, {hum}"
            print(f"Writing [ {data} ] to file {cnf['file name']}")
            f.write(data + "\n")
            sleep_ms(1000)
    except OSError:
        pass
print("Done")