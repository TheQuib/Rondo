---
title: Optional Variables
weight: 2
---

These variables are commented out in the default `config.yml` and don't need to be set unless you want to change Rondo's default behavior. Uncomment and set any that apply to your setup.

## Status LED

*config key: `led_enabled` — type: `bool` — default: `false`*

Controls whether Rondo activates the status LED. When set to `true`, Rondo will drive the GPIO pin defined by `led_pin` to indicate its current state.

```yaml
led_enabled: true
```

See [LED Functionality](../led-functionality) for a full description of the LED states.

## LED Pin

*config key: `led_pin` — type: `int` — default: `23`*

The GPIO pin number connected to your status LED. Only takes effect when `led_enabled` is `true`.

```yaml
led_pin: 23
```

{{< callout type="info" >}}
This uses BCM (Broadcom) GPIO numbering, not physical pin numbering. GPIO 23 corresponds to physical pin 16 on the RPi 3.
{{< /callout >}}

## Button Pin

*config key: `button_pin` — type: `int` — default: `17`*

The GPIO pin number connected to your push button.

```yaml
button_pin: 17
```

GPIO 17 corresponds to physical pin 11 on the RPi 3. If you need to use a different pin, update this value and rewire accordingly. Refer to the [Hardware Setup](../../getting-started/hardware-setup) pinout diagram for physical pin locations.