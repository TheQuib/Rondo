---
title: Global Variables
weight: 2
---

Global variables apply to every host in your inventory. Use these for values that are consistent across all your Pis — things like your API endpoint, authentication key, or any shared payload values.

In Semaphore, global variables are managed through the **Environment** feature.

## Setting up an environment

1. In Semaphore, navigate to **Environment**.
2. Click **New Environment**.
3. Give it a friendly name (e.g. `Rondo Global Config`).
4. Make sure you're adding values under **Extra Variables** — not Survey Variables.
5. Add each variable as a key-value pair.

For example, to share an API URL and key across all hosts:

```json
{
  "api_url": "https://api.example.com",
  "api_key": "your-api-key-here"
}
```

## Using secrets

For sensitive values like API keys, use Semaphore's built-in **Secrets** manager rather than entering them as plain-text Extra Variables. Secrets are encrypted at rest and masked in job output logs.

To use a secret as a variable:

1. Navigate to **Secrets** and create a new secret with your value.
2. Reference it in your Environment configuration by name.

{{< callout type="warning" >}}
Avoid storing API keys or tokens as plain-text Extra Variables. If your Semaphore instance is shared with other users, plain-text values in an Environment are visible to anyone with access to that environment.
{{< /callout >}}

## Environment vs inventory precedence

If the same variable is defined in both an Environment and a host's inventory entry, the **inventory value takes precedence** for that host. This means you can set a sensible global default in the Environment and override it per host in the inventory when needed.