---
linkTitle: "Documentation"
title: Intro
---

Welcome to Rondo documentation!

## What is Rondo?

**Rondo** is a lightweight automation tool that triggers HTTP API calls from a physical button press. It can be deployed at scale across multiple devices using Ansible and Docker.

## The core idea

It's simple: A Raspberry Pi sits at the edge, listens for a button press, and fires and API request to whatever endpoint you point it at. Out of the box, Rondo ships configured for remote door unlocking, passing a `door_id` and `user_id` to an API, but the payload and heads are fully configurable, making it adaptable to any use case that benefits from a physical trigger.

## How it works

When the button is pressed, Rondo's Python application reads your `config.yml` and fires a POST request to your configured `api_url`, using the headers and body variables you've defined. The entire flow, from button press to API call, runs inside a Docker container on the Pi, deployed and managed by an Ansible playbook.

For managing deployments across many devices, Rondo integrates well with Ansible Semaphore, giving you a UI to handle inventory, variables, and job runs without touching a terminal.

## What you'll need

 - A Raspberry Pi (tested on RPi 3)
 - A momentary push button (such as a computer power button)
 - An ansible control node (or Semaphore instance)
 - An HTTP API endpoint to call

## Where to go next
If you're setting up for the first time, head to [Getting Started](./getting-started) to walk through hardware wiring and deployment.

If you're already up and running and want to customize your headers, payload or GPIO pins, jump to [Configuration](./configuration).

If you're managing multiple Pis through Semaphore, the [Semaphore](./semaphore) section covers per-host and global variable setup.