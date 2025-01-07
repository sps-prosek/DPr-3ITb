from machine import Pin
from utime import sleep


class MorseCode:
    # Dictionary mapping characters to their Morse code representations
    # Each letter is represented as dots (.) and dashes (-)
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

    def __init__(self, buzzer_pin, potentiometer_pin) -> None:
        """Initialize MorseCode with buzzer and potentiometer pins
        Args:
            buzzer_pin (int): GPIO pin number for PWM buzzer
            potentiometer_pin (int): GPIO pin number for ADC potentiometer
        """
        pass

    def read_pot(self) -> float:
        """Read potentiometer value and convert to 0-1 range
        Returns:
            float: Normalized potentiometer value (0.0 to 1.0)
        """
        return 0.0

    def play_morse_code(self, char) -> None:
        """Play Morse code pattern for a single character
        Args:
            char (str): Character to convert and play
        Note:
            Dot duration: 0.1s
            Dash duration: 0.3s
            Frequency range: 440-1440 Hz controlled by potentiometer
        """
        pass


# Create instance of MorseCode class here

print("Text to morse code...")
while True:
    try:
        # Get text input from user
        # Convert input to uppercase
        # Play Morse code for each character (add 0.3s duration between characters)
        pass
    except KeyboardInterrupt:
        break
print("Finished.")
