import dht
from machine import Pin
from time import sleep

sensor = dht.DHT11(Pin(1))

while True:
    sensor.measure()
    print(f"temperature: {sensor.temperature()} C,   humidity: {sensor.humidity()} %")
    sleep(5)