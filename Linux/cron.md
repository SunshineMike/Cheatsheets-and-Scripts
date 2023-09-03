# Cron Cheatsheet

A quick reference for managing and utilizing `cron` on Unix-like operating systems.

## Table of Contents
- [Introduction](#introduction)
- [Basic Commands](#basic-commands)
- [Cron Time Syntax](#cron-time-syntax)
- [Special Keywords](#special-keywords)
- [Cron File Locations](#cron-file-locations)
- [Debugging](#debugging)

---

## Introduction

Cron is a time-based job scheduler in Unix-like operating systems. It enables users to schedule jobs to run periodically at fixed times, dates, or intervals.

---

## Basic Commands

### Edit User's Cron Jobs
```bash
crontab -e
```

### List User's Cron Jobs
```bash
crontab -l
```

### Remove User's Cron Jobs
```bash
crontab -r
```

### Run Job Every Minute
```bash
* * * * * command
```

---

## Cron Time Syntax

Field        | Allowed Values
------------ | --------------
Minute       | 0 - 59
Hour         | 0 - 23
Day of Month | 1 - 31
Month        | 1 - 12
Day of Week  | 0 - 7 (Both 0 and 7 represent Sunday)

### Examples:

- Run a job at 3 a.m every day:
  ```bash
  0 3 * * * command
  ```
  
- Run a job every 5 minutes:
  ```bash
  */5 * * * * command
  ```
  
- Run a job at 4:30 p.m on the 15th of every month:
  ```bash
  30 16 15 * * command
  ```

---

## Special Keywords

Keyword | Equivalent
-------  | ----------
@yearly  | `0 0 1 1 *`
@monthly | `0 0 1 * *`
@weekly  | `0 0 * * 0`
@daily   | `0 0 * * *`
@hourly  | `0 * * * *`
@reboot  | Run at startup

---

## Cron File Locations

- System-wide crontab: `/etc/crontab`
- User-specific cron jobs: `/var/spool/cron/crontabs/`
- Cron job directories:
  - `/etc/cron.d/`
  - `/etc/cron.daily/`
  - `/etc/cron.hourly/`
  - `/etc/cron.weekly/`
  - `/etc/cron.monthly/`

---

## Debugging

### Check Cron Service Status
```bash
sudo service cron status
```

### View Cron Logs
```bash
sudo grep CRON /var/log/syslog
```

### Validate Cron File Syntax
```bash
cron-sanity-checker /path/to/file
```
(Note: `cron-sanity-checker` is not a built-in utility; you'd have to install or write it.)

---
