from random import randint, uniform


class neopixelSimulator:
    def __init__(self, n) -> None:
        self.__cnf = [(int(0), int(0), int(0))] * n

    def __len__(self) -> int:
        return len(self.__cnf)

    def __setitem__(self, index: int, val: tuple[int, int, int]) -> None:
        self.__cnf[index] = val

    def __getitem__(self, index: int) -> tuple[int, int, int]:
        return self.__cnf[index]

    def fill(self, pixel: tuple[int, int, int]) -> None:
        n = len(self.__cnf)
        self.__cnf = [pixel] * n

    def __bound(self, value: int):
        return max(0, min(255, value))

    def write(self) -> None:
        n = len(self.__cnf)
        print(" " + "_ " * n)
        print("|", end="")
        for i in self.__cnf:
            print(
                f"\x1b[48;2;{self.__bound(i[0])};{self.__bound(i[1])};{self.__bound(i[2])}m \x1b[0m|",
                end="",
            )
        print("\n " + "⎺ " * n)


class dhtSimulator:
    def __init__(self) -> None:
        self.__temp = uniform(20, 40)
        self.__hum = uniform(40, 80)

    def measure(self) -> None:
        self.__temp = uniform(20, 40)
        self.__hum = uniform(40, 80)

    def temperature(self) -> float:
        return self.__temp

    def humidity(self) -> float:
        return self.__hum


rgbLed = neopixelSimulator(10)
sensor = dhtSimulator()


def green(txt: str):
    return "\033[32m{}\033[00m".format(txt)


def red(txt: str):
    return "\033[31m{}\033[00m".format(txt)


def orange(txt: str):
    return "\033[33m{}\033[00m".format(txt)


def temp(args: list[str]):
    sensor.measure()
    temp = sensor.temperature()
    print(green(f"    Temperature is {temp} °C"))


def humid(args: list[str]):
    sensor.measure()
    hum = sensor.humidity()
    print(green(f"    Humidity is {hum} %"))


def rgb(args: list[str]):
    if "clear" in args:
        for i in range(len(rgbLed)):
            rgbLed[i] = (0, 0, 0)
        rgbLed.write()
        print(green("   Clearing the RGBs."))
        return

    if "random" in args:
        for i in range(len(rgbLed)):
            r = int(randint(0, 255))
            g = int(randint(0, 255))
            b = int(randint(0, 255))
            rgbLed[i] = (r, g, b)
        rgbLed.write()
        print(green("   Randomizing the RGBs."))
        return

    req = {
        "-id": 0,
        "-r": 0,
        "-g": 0,
        "-b": 0,
    }

    for arg in req.keys():
        try:
            idx = args.index(arg)
        except ValueError:
            if arg in ["-id"]:
                print(red("   ERROR") + f" mandatory argument {arg} is missing.")
                return
            else:
                print(
                    orange("   WARNING")
                    + f" argument {arg} missing. Using default value."
                )
                continue
        try:
            req[arg] = int(args[idx + 1])
        except ValueError:
            if arg in ["-id"]:
                print(red("   ERROR") + f" in argument {arg} value parsing.")
                return
            else:
                print(
                    orange("   WARNING")
                    + f" in argument {arg} value parsing. Using default value."
                )
        except IndexError:
            if arg in ["-id"]:
                print(red("   ERROR") + f" missing value at mandatory argument {arg}.")
                return
            else:
                print(
                    orange("   WARNING")
                    + f" missing value at argument {arg}. Using default value."
                )

    id = req["-id"]
    color = (req["-r"], req["-g"], req["-b"])

    if not (0 <= req["-id"] < len(rgbLed)):
        print(red("   RGB LED id out of bounds."))
        return

    if not all([True if 0 <= val <= 255 else False for val in color]):
        print(red("   RGB LED color out of bounds."))
        return

    print(green(f"   Setting RGB led with id = {id} to color = {color}."))

    rgbLed[id] = color
    rgbLed.write()


def help(args: list[str]):
    helpMsg = """

        Argument parser for Rpi pico. Available commands:
            
            rgb - set RGB led on LED stick with 10 RGB LEDs
                clear           - clear all RGB LEDs
                random          - randomize all RGB LEDs
                -id [int 0-9]   - id of RGB to be set                (required)
                -r  [int 0-255] - red part of RGB color to be set    (optional - default 0)
                -g  [int 0-255] - green part of RGB color to be set  (optional - default 0)
                -b  [int 0-255] - blue part of RGB color to be set   (optional - default 0)
            
            temp - print current temperature
            
            humid - print current humidity
            
            help - print help
    
    """
    print(helpMsg)


cmds = {"temp": temp, "humid": humid, "rgb": rgb, "help": help}


def HandleCommand(command, args):
    if command in cmds.keys():
        cmds[command](args)
    else:
        print(red("   Unknown command."))


def main():
    while True:
        user_input = input("Enter command: ")
        parts = user_input.split()

        if parts:
            HandleCommand(parts[0], parts[1:])
        else:
            print(red("   No command entered."))


if __name__ == "__main__":
    main()
