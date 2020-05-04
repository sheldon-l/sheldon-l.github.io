---
layout: post
published_at: "2020-05-01"
updated_at: "2020-05-01"
author: Taners
tags: [Linux, printer]
---

## Introduction to DevOps and SRE

### The Pre-DevOps Era (Before 2007)

- Releases = thriller movie
- Infrastructure is not flexive
- Continuous Integration was in a very nascent stage: Cruise Control, Hudson
- Monitoring: Nagios, didn't have a way to pull out the logs and centrally  manage it.

### Emergence of DevOps

- centralized configuration management system:
  - Puppet, mainly for laptops and desk tops.
  - containers for production systems.
  - Borg, orchestrator for containers
  - `cgroup` kernel offered a process resources isolation.