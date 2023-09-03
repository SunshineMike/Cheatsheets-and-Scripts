# Network Commands Cheatsheet

A quick guide to essential networking commands for Linux and Unix-like systems.

## Table of Contents
1. [Introduction](#introduction)
2. [Network Information](#network-information)
3. [Network Configuration](#network-configuration)
4. [Host Lookup](#host-lookup)
5. [Port Scanning](#port-scanning)
6. [Ping and Reachability](#ping-and-reachability)
7. [Trace Route](#trace-route)
8. [Packet Capture](#packet-capture)
9. [Firewall](#firewall)

---

## Introduction

This cheatsheet provides a quick reference for networking commands commonly used in Linux and Unix-like systems.

---

## Network Information

### `ifconfig` / `ip` — Network Interfaces
```bash
ifconfig
ip addr show
```

### `netstat` — Network Statistics
```bash
netstat -tuln
```

### `ss` — Socket Statistics
```bash
ss -tuln
```

---

## Network Configuration

### `ifconfig` / `ip` — Set IP Address
```bash
sudo ifconfig eth0 192.168.1.2 netmask 255.255.255.0
sudo ip addr add 192.168.1.2/24 dev eth0
```

### `route` / `ip` — Set Default Gateway
```bash
sudo route add default gw 192.168.1.1
sudo ip route add default via 192.168.1.1
```

---

## Host Lookup

### `nslookup` — Query DNS
```bash
nslookup example.com
```

### `dig` — DNS Lookup
```bash
dig example.com
```

### `host` — Simple DNS Lookup
```bash
host example.com
```

---

## Port Scanning

### `nmap` — Port Scanner
```bash
nmap 192.168.1.2
```

### `nc` — Netcat for Port Scanning
```bash
nc -zv 192.168.1.2 80-90
```

---

## Ping and Reachability

### `ping` — Ping Host
```bash
ping example.com
```

### `arp` — Address Resolution Protocol
```bash
arp -a
```

---

## Trace Route

### `traceroute` — Trace Route
```bash
traceroute example.com
```

### `mtr` — Real-time Traceroute
```bash
mtr example.com
```

---

## Packet Capture

### `tcpdump` — Capture Packets
```bash
sudo tcpdump -i eth0
```

### `wireshark` — GUI-based Packet Capture
```bash
wireshark
```

---

## Firewall

### `iptables` — List Firewall Rules
```bash
sudo iptables -L
```

### `ufw` — Uncomplicated Firewall
```bash
sudo ufw status
```

---
