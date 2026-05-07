---
title: Installation
weight: 2
---

Rondo is deployed to your Raspberry Pi using an Ansible playbook. The playbook handles everything — installing Docker, copying files, generating your config, and starting the container.

## Prerequisites

Before running the playbook, make sure you have:

- Ansible installed on your control node
- SSH access to your Raspberry Pi(s)
- Your Pi running Raspberry Pi OS (Debian Bookworm+)
- The `pi` user account available on each Pi

## 1. Clone the repository

```bash
git clone https://github.com/TheQuib/Rondo.git
cd Rondo
```

## 2. Configure your variables

Copy or edit `config.yml` with your environment's values. At minimum, you need to set your API endpoint and key:

```yaml
token_url: "https://api.example.com/token"

token_headers:
  accept: "application/json"
  x-api-key: "{{ api_key }}:"

api_url: "https://api.example.com"

payload:
  payload-1: "your-payload-data"
  payload-2: "your-payload-data"

#led_enabled: true
#led_pin: 23
#button_pin: 17
```

The `config.yml` is processed as a Jinja2 template when deployed, so variables like `{{ api_key }}` will be substituted from your Ansible environment variables. See [Configuration](../configuration) for a full breakdown of all available options.

{{< callout type="warning" >}}
Do not commit secrets like your API key directly to `config.yml`. Pass them through Ansible environment variables or, if using Semaphore, use its built-in secret manager.
{{< /callout >}}

## 3. Set up your Ansible inventory

Add your Pi(s) to an inventory file. A basic static inventory looks like:

```ini
[pis]
pi1 ansible_host=192.168.1.101 ansible_user=pi
pi2 ansible_host=192.168.1.102 ansible_user=pi
```

If you're using Ansible Semaphore to manage your inventory, see the [Semaphore](../semaphore) section instead.

## 4. Run the playbook

```bash
ansible-playbook -i inventory deploy-rondo.yml
```

The playbook will:

1. Install Docker and its dependencies on the Pi
2. Create the `/home/pi/rondo` project directory
3. Copy `docker-compose.yml` to the Pi
4. Generate `config.yml` from the Jinja2 template
5. Pull the latest Rondo container image
6. Start the container with `--force-recreate`
7. Ensure the container is set to restart automatically

## Verifying the deployment

Once the playbook completes, SSH into your Pi and confirm the container is running:

```bash
docker ps
```

You should see the `rondo` container listed with a status of `Up`. If you have `led_enabled: true` in your config, the LED should be solid — indicating Rondo is running and waiting for a button press.