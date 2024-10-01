import os
import dht
from machine import Pin
from time import sleep

run = True

sensor = dht.DHT11(Pin(1))

with open("data.csv", "a") as f:
    while run:
        try:
            sensor.measure()
            print(
                f"temperature: {sensor.temperature()} C,   humidity: {sensor.humidity()} %"
            )
            f.write(f"{sensor.temperature()}, {sensor.humidity()}\n")
            sleep(5)
        except OSError:
            print("Disk full!!!")
            run = False
        except KeyboardInterrupt:
            print("Ending the program...")
            run = False
