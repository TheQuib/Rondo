from gpiozero import Button
import time
from api_handler import APIHandler

class ButtonHandler:
    def __init__(self, gpio_pin=17, debounce_time=1, api_handler=None):
        self.button = Button(gpio_pin)
        self.debounce_time = debounce_time
        self.last_press_time = time.time()
        self.api_handler = api_handler

    def handle_press(self):
        current_time = time.time()
        if current_time - self.last_press_time > self.debounce_time:
            print("Button pressed! Executing API call...")
            if self.api_handler:
                self.api_handler.make_api_call()
            self.last_press_time = current_time

    def start_listening(self):
        self.button.when_pressed = self.handle_press
        print("Waiting for button press...")
        while True:
            time.sleep(1)  # Keep the script running