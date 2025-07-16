from ota import OTAUpdater
from secrets import secrets
from machine import Pin
from time import sleep

# --- OTA Update ---
ota_updater = OTAUpdater(secrets['ssid'], secrets['password'], secrets['url'], secrets['filename'])
ota_updater.download_and_install_update_if_available()

# --- Hardware setup (bare MicroPython) ---

# GPIO Pins
RELAY_1_PIN = 9         # Relay 1 (connected to GP9)
BUTTON_A_PIN = 12       # Button A (SWITCH_A on GP12)

# Setup Relay output
relay_1 = Pin(RELAY_1_PIN, Pin.OUT)
relay_1.off()  # Ensure it's off at boot

# Setup Button input with internal pull-up
button_a = Pin(BUTTON_A_PIN, Pin.IN, Pin.PULL_UP)

print("System ready. Press Button A to activate Relay 1.")

# --- Main loop ---
while True:
    if not button_a.value():  # Button pressed (active low)
        relay_1.on()
    else:
        relay_1.off()

    sleep(0.05)
