import os
from api_handler import APIHandler
from button_handler import ButtonHandler

def simulate_button_press():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "config.yml")

    api_handler = APIHandler(config_file=config_path)
    button_handler = ButtonHandler(api_handler=api_handler)
    button_handler.handle_press()  # Directly trigger the press event

if __name__ == "__main__":
    simulate_button_press()
