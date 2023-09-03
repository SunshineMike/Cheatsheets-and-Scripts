# Process Management Cheatsheet

A quick reference guide for managing processes in Linux and Unix-like operating systems.

## Table of Contents
1. [Introduction](#introduction)
2. [Listing Processes](#listing-processes)
3. [Background and Foreground Processes](#background-and-foreground-processes)
4. [Killing Processes](#killing-processes)
5. [Changing Process Priority](#changing-process-priority)
6. [Monitoring Processes](#monitoring-processes)

---

## Introduction

Managing processes is a critical skill when working with Linux and Unix-like operating systems. This cheatsheet aims to provide a quick reference for common process management tasks.

---

## Listing Processes

### `ps` — Show Current Processes
```bash
ps
ps aux # Detailed list
ps -e # All processes
ps -T # List threads as well
```

### `pgrep` — Search Processes
```bash
pgrep process_name
```

### `pstree` — Tree View of Processes
```bash
pstree
```

---

## Background and Foreground Processes

### `&` — Run in Background
```bash
command &
```

### `bg` — Continue in Background
```bash
bg %job_id
```

### `fg` — Bring to Foreground
```bash
fg %job_id
```

### `jobs` — List Background Jobs
```bash
jobs
```

---

## Killing Processes

### `kill` — Kill by PID
```bash
kill PID
kill -9 PID # Force kill
```

### `pkill` — Kill by Name
```bash
pkill process_name
```

### `killall` — Kill All Instances by Name
```bash
killall process_name
```

---

## Changing Process Priority

### `nice` — Start with Different Priority
```bash
nice -n priority command
```

### `renice` — Change Priority of Running Process
```bash
renice priority -p PID
```

---

## Monitoring Processes

### `top` — Real-time Process Viewer
```bash
top
```

### `htop` — Enhanced Real-time Process Viewer
```bash
htop
```

### `vmstat` — Virtual Memory Statistics
```bash
vmstat
```

### `iotop` — Monitor I/O
```bash
iotop
```

---
