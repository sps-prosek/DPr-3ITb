from machine import Pin
from utime import ticks_ms, sleep


# Class to handle button interrupts and debouncing
class InterruptButton:
    def __init__(self, pin):
        self.pin = Pin(pin, Pin.IN)  # Initialize pin as an input
        self.btnPressed = False  # Flag to indicate button press
        self.lastBtnPressTime = 0  # Record of the last button press time
        # Set up an interrupt for the button on falling edge, using callback
        self.pin.irq(trigger=Pin.IRQ_FALLING, handler=self.callback, hard=True)

    # Callback function for the button interrupt
    def callback(self, pin):
        # Check if enough time has passed to register a new press (debounce)
        if ticks_ms() - self.lastBtnPressTime >= 100:
            self.btnPressed = True  # Set flag to indicate a press
            self.lastBtnPressTime = ticks_ms()  # Update last press time

    # Method to check if the button was pressed
    def was_pressed(self):
        return self.btnPressed

    # Method to clear the button press flag
    def clear(self):
        self.btnPressed = False


# Class to simulate a traffic light with automatic and manual modes
class TrafficLight:
    def __init__(self):
        self.state = "Red"  # Initial traffic light state
        self.mode = "Auto"  # Default mode is automatic
        self.lastLightChangeTime = ticks_ms()  # Track last light change time
        self.show_light()  # Display the initial light

    # Method to cycle through traffic light states
    def next_light(self):
        if self.state == "Red":
            self.state = "Green"
        elif self.state == "Green":
            self.state = "Yellow"
        elif self.state == "Yellow":
            self.state = "Red"
        self.show_light()  # Print the current state

    # Method to display the current light state
    def show_light(self):
        print("Traffic Light: " + self.state)

    # Toggle between automatic and manual mode
    def toggle_manual_mode(self):
        if self.mode == "Auto":
            self.mode = "Manual"
        else:
            self.mode = "Auto"
            self.lastLightChangeTime = ticks_ms()  # Reset change time in Auto
        print("Mode Switched to " + self.mode)

    # Automatically switch lights if in Auto mode
    def run_auto(self):
        if self.mode == "Auto":
            # Check if 3 seconds have passed since the last light change
            if ticks_ms() - self.lastLightChangeTime >= 3000:
                self.next_light()  # Cycle to the next light
                self.lastLightChangeTime = ticks_ms()  # Update last change time


# Main program setup
print("Traffic Light System Starting in Auto Mode")

tl = TrafficLight()  # Initialize TrafficLight instance
modeSwitchBtn = InterruptButton(20)  # Button to switch between modes
manualBtn = InterruptButton(21)  # Button to change light in Manual mode

# Main loop to handle button presses and automatic light control
while True:
    try:
        # Check if mode switch button was pressed
        if modeSwitchBtn.was_pressed():
            tl.toggle_manual_mode()  # Toggle between Auto and Manual
            modeSwitchBtn.clear()  # Clear button press flag

        # Check if manual light change button was pressed
        if manualBtn.was_pressed():
            # Only allow manual light change if in Manual mode
            if tl.mode == "Auto":
                print("Manual control is forbidden in automatic mode.")
            else:
                tl.next_light()  # Change light manually
            manualBtn.clear()  # Clear button press flag

        # Run automatic light change if in Auto mode
        tl.run_auto()

    except KeyboardInterrupt:
        break  # Exit loop on keyboard interrupt

print("Finished.")  # Indicate program end
