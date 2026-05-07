---
title: About
weight: 2
toc: false
sidebar:
  hide: true
---

Rondo started with a pretty common problem: I needed a way to remotely unlock doors, and every "smart" solution on the market either cost a fortune, required a proprietary hub, or meant running new wiring through walls I didn't want to tear open.

Most commercial access control systems are built for enterprises — and priced accordingly. The affordable consumer options tend to lock you into a specific ecosystem, require a cloud subscription, or just don't offer the flexibility to integrate with an existing API. None of that was going to work.

The alternative — running proper access control cabling — wasn't much better. That means conduit, cable pulls, and either hiring someone or spending a weekend inside walls. For a setup that just needs to trigger a door release, that felt like massive overkill.

## The actual solution

A Raspberry Pi, a button, and a few jumper wires turned out to be all that was needed. The Pi sits near the door, listens for a button press, and fires a POST request to an API that handles the unlock. No proprietary hub, no subscription, no new cabling — just a small device plugged into power and connected to the network.

The button is wired directly to the Pi's GPIO pins. The whole thing runs in a Docker container, deployed and managed with Ansible so it's easy to push updates or roll out to new devices without touching each one individually.

## Why Ansible?

Once it became clear that this could scale to multiple doors, managing each Pi by hand stopped being realistic. Ansible lets me treat every Pi the same way — one playbook run pushes the latest config and restarts the container across the whole fleet. Semaphore puts a UI on top of that so it doesn't require a terminal every time.

## The name

[Rondo](https://en.wikipedia.org/wiki/Rondo) is a musical form where a main theme keeps returning throughout a piece — it repeats. Felt fitting for something that sits in a loop, waiting to do the same thing over and over.