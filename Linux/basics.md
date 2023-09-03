# Linux Basic CLI Commands Cheatsheet

A comprehensive reference guide for essential Linux command-line interface (CLI) commands.

## Table of Contents
1. [File Operations](#file-operations)
2. [Directory Operations](#directory-operations)
3. [File Permissions](#file-permissions)
4. [Searching](#searching)
5. [System Info](#system-info)
6. [Package Management](#package-management)
7. [Process Management](#process-management)
8. [Networking](#networking)
9. [Disk Operations](#disk-operations)
10. [Compression](#compression)
11. [Text Processing](#text-processing)
12. [Other Utilities](#other-utilities)

---

## File Operations

### `ls` - List Files
```bash
ls
ls -l # Long listing
ls -a # Include hidden files
```

### `cp` - Copy Files
```bash
cp source destination
```

### `mv` - Move Files
```bash
mv source destination
```

### `rm` - Remove Files
```bash
rm file
rm -r directory # Recursive
```

### `touch` - Create Empty File
```bash
touch filename
```

### `cat` - Display File Content
```bash
cat filename
```

---

## Directory Operations

### `pwd` - Current Directory
```bash
pwd
```

### `cd` - Change Directory
```bash
cd directory
cd ~  # Home directory
```

### `mkdir` - Make Directory
```bash
mkdir directory
```

### `rmdir` - Remove Directory
```bash
rmdir directory
rm -rf directory # Recursive !!!
```

---

## File Permissions

### `chmod` - Change Mode
```bash
chmod 755 filename
```

### `chown` - Change Owner
```bash
chown username:group filename
```

---

## Searching

### `find` - Find Files
```bash
find /path -name filename
```

### `grep` - Search Within Files
```bash
grep pattern filename
```

---

## System Info

### `uname` - System Information
```bash
uname -a
```

### `df` - Disk Free
```bash
df -h
```

### `free` - Memory Info
```bash
free -m
```

### `top` - Task Manager
```bash
top
```

### `lscpu` - CPU Info
```bash
lscpu
```

---

## Package Management

### `apt` - (Debian-based)
```bash
sudo apt update
sudo apt upgrade
sudo apt install package
sudo apt remove package
```

### `yum` - (Red Hat-based)
```bash
sudo yum install package
sudo yum remove package
```

---

## Process Management

### `ps` - Process Status
```bash
ps aux
```

### `kill` - Kill Process
```bash
kill PID
```

### `bg` & `fg` - Background and Foreground
```bash
bg %job_number
fg %job_number
```

---

## Networking

### `ping` - Test Connectivity
```bash
ping host
```

### `ifconfig` / `ip` - Interface Configuration
```bash
ifconfig
ip addr
```

### `ssh` - Secure Shell
```bash
ssh username@host
```

### `scp` - Secure Copy
```bash
scp source username@host:destination
```

---

## Disk Operations

### `fdisk` - Disk Partition
```bash
sudo fdisk -l
```

### `dd` - Disk Dump
```bash
dd if=input of=output
```

---

## Compression

### `tar` - Archive Files
```bash
tar -cvf archive.tar files/
tar -xvf archive.tar
```

### `gzip` - Compress File
```bash
gzip file
```

### `gunzip` - Decompress File
```bash
gunzip file.gz
```

---

## Text Processing

### `sed` - Stream Editor
```bash
sed 's/old/new/g' filename
```

### `awk` - Text Processing
```bash
awk '{print $1}' filename
```

### `sort` - Sort Lines
```bash
sort filename
```

### `wc` - Word Count
```bash
wc filename
```

---

## Other Utilities

### `echo` - Display Text
```bash
echo "text"
```

### `date` - Display Date
```bash
date
```

### `cal` - Display Calendar
```bash
cal
```

### `alias` - Create Alias
```bash
alias short='long-command'
```

---
