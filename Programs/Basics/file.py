import os
from time import sleep

fileName = "data.txt"

with open(fileName, "w") as f:
    try:
        f.write("Hello from rpi pico...\n")
        for i in range(6):
            print(f"Writing i = {i} to file {fileName}")
            f.write(str(i) + "\n")
            sleep(1)
    except OSError:
        pass
print("Done")