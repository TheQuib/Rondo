# Rondo
Trigger API calls at scale with just a Raspberry Pi, a button, and Ansible.

Out of the box, the packaged Ansible Playbook and Docker Container will make an API call to a specified endpoint with an API key, passing out `user_id` and `door_id` variables, designed to unlock doors remotely using a button.

# tl;dr
 - Rondo will make API calls to an endpoint using custom headers and payloads.
 - The `config.yml` file contains each variable that can be set. Add / remove the variables you want to specify for the headers and the body.
 - Once you are satisfied with the variables, add them into Ansible as environment variables (store them as you please, hopefully securely). **IF USING ANSIBLE SEMAPHORE**: Use extra secret variables or inventory host variables ([explained below](#modifying-variables))

# Setup
## Variables
At base level, you will need:

**Required:**
 - `api_url`, *string*: The API endpoint URL Python will make calls to.
 - `x-api-key`, *string*: The API key Python will use to authenticate to the API.
 - `door_id`, *string*: The ID of the door to unlock.
 - `user_id`, *string*: The ID of the user that will unlock the door.

**Optional:**
 - `led_enabled`, *bool*: If you want to enable status LED functionality
   - *Default*: `false`
 - `led_pin`, *int*: GPIO pin for LED connection
   - *Default*: `23`
 - `button_pin`, *int*: GPIO pin for button connection
   - *Default*: `17`

## Modifying variables
The variables in the configuration can be modified to your use case. Add or remove them, and the script will update the headers and body accordingly.

## Configure Variables in Semaphore UI
There are two type of variables that you can configure in Semaphore:
 - Per host
 - Globally

### Per host variables
Configure per host variables using the Ansible inventory.

In Semaphore:
 - Navigate to `Inventory`.
 - Go to `New Inventory` > `Ansible Inventory`.
 - Give it a friendly name.
 - Select credentials as necessary.
 - Select `Static YAML` as the type.
 - Use the following template.
   - Set variables that you want to change per host as desired.
```yaml
notes:
  hosts:
    pi1:
      ansible_host: 192.168.1.101
      ansible_user: pi
      DOOR_ID: e3a1d7f9-6b3c-4f59-b813-1a728a214d89
      USER_ID: pi1_user
    pi2:
      ansible_host: 192.168.1.102
      ansible_user: pi
      DOOR_ID: e3a1d7f9-6b3c-4f59-b813-1a728a214d89
      USER_ID: pi2_user
    pi3:
      ansible_host: 192.168.1.103
      ansible_user: pi
      DOOR_ID: 7c5e8a92-2b41-4de6-8a3f-4d182bb5f2e9
      USER_ID: pi3_user
```


### Global variabes
Configure global variables (variables that will apply to all hosts) using Semaphore's *Environment* feature.

In Semaphore:
 - Navigate to `Environment`.
 - Go to `New Environment`.
 - Give it a friendly name.
 - For each variable you want to configure for all hosts, make sure you're configuring `Extra Variables`.
 - Use `Secrets` if you want to use Semaphore's built-in secret manager.

## LED functionality
If the `led_enabled` variable is set to `true`, a status LED is triggered on GPIO pin 23 (set by the `led_pin` variable if you wish to change it).

Current statuses:
 - *Solid*: `main.py` is running, awaiting a button press.
 - *Blinking*: Button has been pressed and `button_handler.py` is currently running API actions.