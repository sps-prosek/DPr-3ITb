# Assignment: Traffic Light Simulation with Classes and Button Control

## Objective

Create a program to simulate a traffic light system using classes, object-oriented programming, and button inputs on the Raspberry Pi Pico. Represent the traffic light colors with print statements.

## Requirements

Develop a `TrafficLight` class and a program that uses button inputs to control the sequence of traffic light colors (Red → Green → Yellow → Red). Each light color should be represented by a unique print message to indicate the current light status.

## Expected Skills

- Object-oriented programming (OOP)
- Handling button inputs with interrupts

## Instructions

### 1. Setting up the TrafficLight Class

1. Create a new file on your Raspberry Pi Pico.
2. Define a `TrafficLight` class with the following structure:
    - An `__init__` method that initializes the traffic light state to "Red" and sets the manual mode to False.
    - A `next_light` method that moves through the traffic light sequence.
    - A `show_light` method that prints the current light state.
    - A `toggle_manual_mode` method that toggles between automatic and manual mode, with a print statement indicating the active mode.

### 2. Adding Button Control

1. Connect two buttons to your Raspberry Pi Pico. One button will toggle between manual and automatic mode, and the other will change the traffic light to the next color in manual mode.
2. Set up interrupts for both buttons:
    - The first button should call `toggle_manual_mode` to switch between modes.
    - The second button should call `next_light` to change the light color in manual mode. If pressed in automatic mode, it should print a message indicating that manual control is forbidden.

### 3. Automatic Light Switching

1. In automatic mode, the traffic light should switch through the sequence every few seconds without any button presses. Add a timer to do this.
2. Use a loop or timer that calls the `next_light` method every 3 seconds when in automatic mode.

### Program Flow

1. Start the program and observe the initial state of the traffic light by looking at the printed messages.
2. Each time you press the mode button, the traffic light will toggle between automatic and manual mode.
3. In manual mode, pressing the second button will switch to the next color.
4. In automatic mode, pressing the second button will print a message indicating that manual control is forbidden.
5. In automatic mode, the traffic light will automatically switch colors every few seconds.

### Expected Output

When you run the program, you should see a sequence like this in the console:

```
Traffic Light: Red
Traffic Light: Green
Traffic Light: Yellow
Traffic Light: Red
```

If manual mode is activated, the button should change the color in this sequence, while automatic mode should run the sequence on a timer. If the manual control button is pressed in automatic mode, you should see a message like:

```
Manual control is forbidden in automatic mode.
```

## Additional Resources

To help you complete this assignment, here are some additional resources you might find useful:

- [MicroPython Documentation](https://docs.micropython.org/en/latest/rp2/quickref.html)
- [Python Classes and Object-Oriented Programming](https://docs.python.org/3/tutorial/classes.html)

## Troubleshooting Tips

- **Button Not Responding:** Ensure that the buttons are properly connected to the GPIO pins and that you have configured the correct pin numbers in your code.
- **Traffic Light Not Switching Automatically:** Check that the timer is correctly implemented and that the `next_light` method is being called at the correct intervals.
- **Incorrect Light Sequence:** Verify the logic in the `next_light` method to ensure it follows the correct sequence (Red → Green → Yellow → Red).

## Submission

Submit your completed code to moodle with name ```TEST1_NAME_SURNAME.py```

