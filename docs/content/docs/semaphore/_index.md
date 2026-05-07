---
title: Semaphore
weight: 4
---

[Ansible Semaphore](https://semaphoreui.com/) is an open-source UI for running Ansible playbooks. If you're managing Rondo across multiple Raspberry Pis, Semaphore lets you handle inventory, variables, and deployments without touching a terminal.

This section covers how to configure Rondo's variables within Semaphore specifically. If you haven't set up Semaphore yet, refer to the [Semaphore documentation](https://docs.semaphoreui.com/) to get an instance running first.

## Variable types in Semaphore

Semaphore gives you two places to define variables for Rondo:

- **Per-host variables** — set via the Ansible Inventory. Use these for values that differ between Pis, like `door_id` or `user_id`.
- **Global variables** — set via Semaphore's Environment feature. Use these for values that are the same across all Pis, like your `api_url` or `x-api-key`.

The pages in this section cover each approach:

- **[Per-Host Variables](./per-host-variables)** — Configuring host-specific values through the Semaphore inventory.
- **[Global Variables](./global-variables)** — Configuring shared values through Semaphore's Environment feature.