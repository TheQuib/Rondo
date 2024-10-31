from gpiozero import Button, LED
import time
from threading import Thread
from api_handler import APIHandler

class ButtonHandler:
    def __init__(self, api_handler=None, gpio_pin=17, debounce_time=1, led_pin=23, led_enabled=False):
        self.button = Button(gpio_pin, pull_up=True)  # Default to GPIO pin 17 for button
        self.debounce_time = debounce_time
        self.last_press_time = time.time()
        self.api_handler = api_handler
        self.led_enabled = led_enabled
        self.led = LED(led_pin) if led_enabled else None  # Default to GPIO pin 23 for LED

        if self.led_enabled:
            self.led.off()  # Start with the LED off, indicating the script is not running

    def handle_press(self):
        current_time = time.time()
        if current_time - self.last_press_time > self.debounce_time:
            print("Button pressed! Executing API call...")
            if self.api_handler:
                self.blink_led()  # Start blinking LED when API call is triggered
                Thread(target=self.api_handler.make_api_call).start()  # Run the API call in a separate thread
            self.last_press_time = current_time

    def start_listening(self):
        if self.led_enabled:
            self.led.on()  # Turn LED on (solid) when the program is ready to receive input
        print("Setting button press handler...")

        self.button.when_pressed = self.handle_press  # Ensure the press handler is being set
        print("Waiting for button press...")

        while True:
            time.sleep(1)  # Keep the script running

    def blink_led(self):
        if self.led_enabled:
            def blink():
                for _ in range(5):  # Blink 5 times
                    self.led.on()
                    time.sleep(0.2)
                    self.led.off()
                    time.sleep(0.2)
                self.led.on()  # Set the LED back to solid after blinking
            Thread(target=blink).start()

    def stop(self):
        if self.led_enabled:
            self.led.off()  # Turn off LED when the script stops