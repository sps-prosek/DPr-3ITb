from machine import Pin, PWM, ADC
from utime import sleep, ticks_ms


class MorseCode:
    MORSE = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        " ": " ",
    }

    def __init__(self, buzzer_pin, potentiometer_pin):
        self.buzzer = PWM(Pin(buzzer_pin))
        self.potentiometer = ADC(Pin(potentiometer_pin))

    def read_pot(self):
        return self.potentiometer.read_u16() / 65535

    def play_morse_code(self, char):
        base_freq = 440
        timing = 0.1

        freq = base_freq + (self.read_pot() * 1000)

        self.buzzer.freq(int(freq))

        for symbol in self.MORSE.get(char, ""):
            if symbol == ".":
                self.buzzer.duty_u16(2000)
                sleep(timing)
            else:
                self.buzzer.duty_u16(2000)
                sleep(timing * 3)
            self.buzzer.duty_u16(0)
            sleep(timing)
        sleep(timing * 3)


morse = MorseCode(18, 27)

print("Text to morse code...")
while True:
    try:
        input_text = input("Enter text: ").upper()
        for char in input_text:
            morse.play_morse_code(char)
    except KeyboardInterrupt:
        break
print("Finished.")
