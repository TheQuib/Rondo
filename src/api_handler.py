import os
import requests
import yaml
import json

class APIHandler:
    def __init__(self, config_file="config.yml"):
        if not os.path.exists(config_file):
            raise FileNotFoundError(f"Configuration file {config_file} not found. Please provide a valid configuration file.")

        self.config = self.load_config(config_file)
        #self.validate_config()

    def load_config(self, config_file):
        with open(config_file, 'r') as file:
            return yaml.safe_load(file)

    def validate_config(self):
        required_keys = ['api_url', 'payload']
        for key in required_keys:
            if key not in self.config:
                raise ValueError(f"Missing required config key: {key}")

        # Validate headers and payload are dictionaries
        if not isinstance(self.config['payload'], dict):
            raise ValueError("Payload must be a dictionary")

        # Check required payload field
        payload_keys = ['door_id', 'user_id']  # Update according to your specific payload structure

        for key in payload_keys:
            if key not in self.config['payload']:
                raise ValueError(f"Missing required payload key: {key}")

    def make_api_call(self):
        try:
            # Retrieve token
            tokenRequest = requests.post(
                url=self.config['token_url'],
                headers=self.config['token_headers']
            )
            token = tokenRequest.json().get("token")
            # Make call
            response = requests.post(
                url=self.config['api_url'],
                headers={"accept": "application/json", "content-type": "application/json", "x-verkada-auth": token},
                json=self.config['payload']
            )
            response.raise_for_status()
            print(f"API call successful: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return None