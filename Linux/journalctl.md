# journalctl Cheatsheet

A quick reference for managing and querying logs with `journalctl` on systemd-based Linux systems.

## Table of Contents
1. [Introduction](#introduction)
2. [Basic Commands](#basic-commands)
3. [Time Filters](#time-filters)
4. [Unit Filters](#unit-filters)
5. [Priority Levels](#priority-levels)
6. [Output Formats](#output-formats)
7. [Disk Usage](#disk-usage)
8. [Additional Features](#additional-features)

---

## Introduction

`journalctl` is a command-line utility for querying and displaying logs from `systemd`'s journal. The journal is stored in a binary format and can be queried in various ways.

---

## Basic Commands

### Show all collected logs
```bash
journalctl
```

### Follow new log messages
```bash
journalctl -f
```

### Show kernel ring buffer messages (dmesg)
```bash
journalctl -k
```

### Show logs since last boot
```bash
journalctl -b
```

### Show logs for a specific unit
```bash
journalctl -u unit-name
```

### Show logs for a specific user
```bash
journalctl _UID=user_id
```

### Show logs for a specific process
```bash
journalctl _PID=process_id
```

---

## Time Filters

### Show logs since a specific date and time
```bash
journalctl --since="YYYY-MM-DD HH:MM:SS"
```

### Show logs until a specific date and time
```bash
journalctl --until="YYYY-MM-DD HH:MM:SS"
```

---

## Unit Filters

### Show logs from a particular systemd service
```bash
journalctl -u service-name.service
```

### Exclude logs of a particular systemd service
```bash
journalctl -u service-name.service --invert-match
```

---

## Priority Levels

Logs can be filtered by priority level, from 0 (emerg) to 7 (debug).

### Show logs of a specific priority
```bash
journalctl -p err
```

---

## Output Formats

### Show logs in JSON format
```bash
journalctl -o json
```

### Short, with date but no time
```bash
journalctl -o short-iso
```

---

## Disk Usage

### Show journal disk usage
```bash
journalctl --disk-usage
```

### Vacuum journal files to reduce disk usage
```bash
journalctl --vacuum-size=1G
```

---

## Additional Features

### Refresh metadata catalog (for quicker searches)
```bash
journalctl --update-catalog
```

### Export entries to a binary journal file
```bash
journalctl -o export -n 100 > some-file.journal
```

---
