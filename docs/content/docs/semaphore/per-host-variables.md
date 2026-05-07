---
title: Per-Host Variables
weight: 1
---

Per-host variables are values that differ between individual Pis — for example, each Pi might control a different door, so each needs its own `door_id` and `user_id`. In Semaphore, these are defined directly in the Ansible inventory.

## Setting up the inventory

1. In Semaphore, navigate to **Inventory**.
2. Click **New Inventory** → **Ansible Inventory**.
3. Give it a friendly name (e.g. `Rondo Hosts`).
4. Select your credentials as needed.
5. Set the type to **Static YAML**.
6. Paste and fill in the following template:

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

Add or remove hosts as needed. Each host entry can carry any variable you want to vary per device.

## How it works

When the Ansible playbook runs, the values defined here are available as host variables. The `config.yml.j2` Jinja2 template uses them to render a unique `config.yml` for each Pi at deploy time — so `pi1` and `pi2` can share a door while `pi3` controls a completely different one, all from a single playbook run.

{{< callout type="info" >}}
Variables set in the inventory are specific to the host they're defined on. If you have a variable that should be the same across all Pis, use a [Global Variable](../global-variables) instead to avoid repeating yourself.
{{< /callout >}}