---
title: Required Variables
weight: 1
---

The following variables must be present in `config.yml` for Rondo to start successfully. Missing any of these will prevent the container from making API calls.

## Token URL

*config key: `token_url` — type: `string`*

The URL Rondo uses to obtain an authentication token before making its main API call.

```yaml
token_url: "https://api.example.com/token"
```

## Authentication Headers

*config key: `token_headers` — type: `map`*

A set of key-value pairs sent as headers with the token request. At minimum this should include your `accept` type and API key.

```yaml
token_headers:
  accept: "application/json"
  x-api-key: "{{ api_key }}"
```

{{< callout type="info" >}}
`{{ api_key }}` is a Jinja2 template variable. Its value is injected at deploy time from your Ansible environment. Never hardcode secrets directly in this file.
{{< /callout >}}

## API Endpoint

*config key: `api_url` — type: `string`*

The endpoint Rondo sends the main API request to when the button is pressed.

```yaml
api_url: "https://api.example.com"
```

## Request Payload

*config key: `payload` — type: `map`*

The key-value pairs sent as the body of the API request. You can add or remove entries freely — Rondo will construct the request body from whatever keys are present here.

```yaml
payload:
  payload-1: "your-payload-data"
  payload-2: "your-payload-data"
```

For the default door-unlock use case, this is where you'd pass your `door_id` and `user_id`:

```yaml
payload:
  door_id: "{{ door_id }}"
  user_id: "{{ user_id }}"
```

Again, using Jinja2 variables here lets you set different values per host through Ansible inventory or Semaphore — useful when managing multiple Pis that each control a different door.