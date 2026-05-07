---
title: Configuration
weight: 3
---

Rondo's behavior is controlled entirely through a single `config.yml` file at the root of the project. This file defines your API endpoint, authentication headers, request payload, and optional hardware settings.

When the Ansible playbook runs, `config.yml` is processed as a Jinja2 template and deployed to `/home/pi/rondo/config.yml` on each target Pi. This means you can use `{{ variable_name }}` syntax to inject secrets and per-host values at deploy time rather than hardcoding them.

The pages in this section cover each part of the config in detail:

- **[Required Variables](./required-variables)** — The minimum set of values needed to make Rondo work.
- **[Optional Variables](./optional-variables)** — GPIO pin overrides and other tuneable settings.
- **[LED Functionality](./led-functionality)** — How to enable and use the status LED.