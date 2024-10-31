import os
from api_handler import APIHandler
from button_handler import ButtonHandler
import yaml

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "config.yml")

    # Load config to check for pin numbers and LED status
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    api_handler = APIHandler(config_file=config_path)

    # Get pin numbers from config or use defaults
    button_pin = config.get('button_pin', 17)  # Default to pin 17 if not in config
    led_pin = config.get('led_pin', 23)  # Default to pin 23 if not in config
    led_enabled = config.get('led_enabled', False)

    # Initialize ButtonHandler with button_pin and led_pin
    button_handler = ButtonHandler(
        api_handler=api_handler,
        gpio_pin=button_pin,  # Pass button pin from config
        led_pin=led_pin,      # Pass LED pin from config
        led_enabled=led_enabled  # Enable or disable LED from config
    )

    try:
        button_handler.start_listening()
    except KeyboardInterrupt:
        button_handler.stop()

if __name__ == "__main__":
    main()