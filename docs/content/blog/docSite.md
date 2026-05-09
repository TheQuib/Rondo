---
title: "Documentation site!"
date: 2024-09-08
authors:
  - name: Quinn Henry
    link: https://github.com/TheQuib
    image: https://avatars.githubusercontent.com/u/78760148
tags:
  - Information
---

When I first put Rondo together, the README made sense. It was a small project, the setup was straightforward enough, and a single markdown file felt like plenty. But as the project grew — more configuration options, Semaphore support, LED functionality, multiple deployment scenarios — the README started turning into a wall of text that was hard to navigate and harder to maintain.

So I built a proper documentation site.

<!--more-->

## What's here

The site covers everything you need to get Rondo running and configured:

- **Getting Started** walks through hardware wiring and deploying with Ansible from scratch
- **Configuration** breaks down every variable in `config.yml`, what it does, and when you'd use it
- **Semaphore** covers managing multi-Pi deployments through Ansible Semaphore, including per-host and global variable setup

It's the same information that was in the README, just organized in a way that's actually easy to navigate — especially once you're past the initial setup and just need to look something up quickly.

## The README isn't going away

The README will stick around as a quick project summary and a pointer to this site. But going forward, all documentation updates will happen here. If something's missing, outdated, or unclear, this is where the fix will land — not in the README.

## What's next

I always say, there's always something to document, so I will keep this site updated and moving forward where I see a need. If there's something specific you'd like covered, open an issue on the [GitHub repo](https://github.com/TheQuib/Rondo) with the `documentation` tag.