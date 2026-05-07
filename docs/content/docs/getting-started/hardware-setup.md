---
title: Hardware Setup
weight: 1
---

Before deploying Rondo, you'll need to wire your button (and optionally an LED) to the Raspberry Pi's GPIO pins.

## What you'll need

- Raspberry Pi (tested on RPi 3)
- Momentary push button
- Jumper wires
- *(Optional)* LED and resistor for status light

## Default pin configuration

Rondo uses the following GPIO pins out of the box:

| Component | GPIO Pin |
|-----------|----------|
| Button    | 17       |
| LED       | 23       |

Both pins are configurable in `config.yml` via the `button_pin` and `led_pin` variables if you need to use different pins. See [Configuration](../configuration) for details.

## Wiring

Connect your button between **GPIO 17** and a **Ground** pin. Connect your LED (with an appropriate current-limiting resistor) between **GPIO 23** and **Ground** if you're using status light functionality.

The diagram below shows the default pin locations on an RPi 3:

![RPi3 GPIO Pinout](https://github.com/TheQuib/Rondo/raw/main/rpi3-gpio-pinout.png)

{{< callout type="info" >}}
If you're using a different Raspberry Pi model, the physical pin layout may differ but the GPIO numbering remains the same.
{{< /callout >}}

## Next steps

Once your hardware is wired up, move on to [Installation](../installation) to deploy Rondo to your Pi.