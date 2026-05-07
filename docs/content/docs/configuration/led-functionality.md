---
title: LED Functionality
weight: 3
---

Rondo includes optional status LED support to give you a physical indicator of what the application is doing. This is useful when a Pi is deployed headlessly and you need to confirm it's running without SSH-ing in.

## Enabling the LED

Set `led_enabled` to `true` in `config.yml`:

```yaml
led_enabled: true
led_pin: 23     # optional, 23 is the default
```

Then redeploy using the Ansible playbook so the updated config is pushed to the Pi:

```bash
ansible-playbook -i inventory deploy-rondo.yml
```

## LED states

| State      | Meaning                                                                 |
|------------|-------------------------------------------------------------------------|
| **Solid**  | `main.py` is running and waiting for a button press                     |
| **Blinking** | Button has been pressed; `button_handler.py` is currently executing the API call |

The LED returns to solid once the API call completes and Rondo is back to listening.

## Wiring

Connect your LED between the GPIO pin defined by `led_pin` and a Ground pin, with a current-limiting resistor in series (typically 220–330Ω for a standard 3.3V GPIO output).

If you haven't wired your LED yet, refer back to the [Hardware Setup](../../getting-started/hardware-setup) page for the default pin locations on the RPi 3.

## GPIO cleanup

When the Rondo container shuts down, the GPIO pins are cleaned up automatically so the LED turns off and the pins are released. If you notice the LED staying on after stopping the container, ensure you're running a recent version — this was fixed in [v2.1.0](../../changelog).