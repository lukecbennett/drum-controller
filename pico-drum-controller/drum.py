from machine import Pin
import time

# Pin Definitions
RELAY_1_PIN = 9      # GPIO controlling Relay 1
BUTTON_A_PIN = 12    # GPIO for Switch A (Button A)

# Set up the relay as an output
relay1 = Pin(RELAY_1_PIN, Pin.OUT)
relay1.value(0)  # Start with relay off

# Set up the button as input with pull-up
button_a = Pin(BUTTON_A_PIN, Pin.IN, Pin.PULL_UP)

print("Press Button A to activate Relay 1")

while True:
    if button_a.value() == 0:  # Button A is pressed (active low)
        print("Button A pressed – activating relay")
        relay1.value(1)        # Turn relay on
    else:
        relay1.value(0)        # Turn relay off

    time.sleep(0.1)

