# Samba & Samba Monitoring Cheatsheet

A collection of useful command-line interface (CLI) commands for managing and monitoring Samba.

## Table of Contents
1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Service Management](#service-management)
4. [User Management](#user-management)
5. [Testing and Validation](#testing-and-validation)
6. [File Sharing](#file-sharing)
7. [Monitoring and Logs](#monitoring-and-logs)


## Installation

### Install Samba on Ubuntu/Debian
```bash
sudo apt update
sudo apt install samba
```

---

## Configuration

### Open Samba configuration file
```bash
sudo nano /etc/samba/smb.conf
```

### Backup Samba configuration file
```bash
sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.bak
```

### Reload Samba Configuration without restarting service
```bash
sudo smbcontrol all reload-config
```

---

## Service Management

### Start Samba Service
```bash
sudo service smbd start
```

### Stop Samba Service
```bash
sudo service smbd stop
```

### Restart Samba Service
```bash
sudo service smbd restart
```

### Check Samba Service Status
```bash
sudo service smbd status
```

---

## User Management

### Add Samba User
```bash
sudo smbpasswd -a username
```

### Delete Samba User
```bash
sudo smbpasswd -x username
```

### Enable/Disable Samba User
```bash
sudo smbpasswd -e username # Enable
sudo smbpasswd -d username # Disable
```

---

## Testing and Validation

### Test Samba Configuration
```bash
testparm
```

### List Shares Accessible by a User
```bash
smbclient -L //localhost -U username
```

### Connect to a Samba Share
```bash
smbclient //server/share -U username
```

---

## File Sharing

### Change Shared Directory Permissions
```bash
chmod -R 0777 /path/to/share
```

### Change Ownership of Shared Directory
```bash
chown -R username:group /path/to/share
```

---

## Monitoring and Logs

### Tail Samba Logs
```bash
tail -f /var/log/samba/log.smbd
```

### Check Samba Version
```bash
smbd --version
```

### Show Active Samba Connections
```bash
sudo smbstatus
```

### Monitor Samba I/O
```bash
iotop -oPa -u smbd
```

---

That's it! This cheatsheet should provide a good starting point for managing and monitoring Samba using CLI commands.
```

Copy this content into a Markdown `.md` file to keep it as a handy reference. This cheatsheet is not exhaustive but should cover the most commonly used commands.
