# Assignment: Text to Morse Code Converter with Classes

## Objective
Create a text-to-Morse-code converter using classes, object-oriented programming, and potentiometer control on the Raspberry Pi Pico.

## Requirements
Develop a `MorseCode` class that converts text to audible Morse code signals with frequency control via potentiometer.

## Expected Skills
- Object-oriented programming (OOP)
- Hardware interaction (PWM, ADC)

## Instructions

### 1. Setting up the MorseCode Class
1. Create a new project for your Raspberry Pi Pico.
2. Finish the `MorseCode` class that is provided in the `test2_base.py` file.
   - Implement potentiometer reading to control frequency (440-1440 Hz)
   - Set up correct timing for dots (0.1s) and dashes (0.3s)

### Program Flow
1. Create `MorseCode` instance
2. Accept text input via terminal
3. Convert each character to Morse code
4. Play corresponding signals through buzzer
5. Adjust frequency using potentiometer

### Expected Output
```
Text to morse code...
Enter text: HELLO
# Plays corresponding Morse code sounds
# Frequency adjusts with potentiometer
```

## Additional Resources
- [MicroPython Documentation](https://docs.micropython.org/en/latest/rp2/quickref.html)
- [Python Classes Documentation](https://docs.python.org/3/tutorial/classes.html)

## Troubleshooting Tips
- **No Sound:** Check buzzer connections and PWM setup
- **Incorrect Frequency:** Verify potentiometer readings
- **Wrong Timing:** Check sleep durations for dots/dashes

## Submission
Submit your code to moodle as `TEST2_NAME_SURNAME.py`