# User Management Cheatsheet

A concise guide for managing user accounts in Linux and Unix-like operating systems.

## Table of Contents
1. [Introduction](#introduction)
2. [Adding Users](#adding-users)
3. [Deleting Users](#deleting-users)
4. [Modifying Users](#modifying-users)
5. [User Groups](#user-groups)
6. [Password Management](#password-management)
7. [Switching Users](#switching-users)
8. [User Information](#user-information)

---

## Introduction

User management involves creating, deleting, and managing user accounts. This cheatsheet serves as a quick reference for user management commands in Linux and Unix-like systems.

---

## Adding Users

### `useradd` — Add New User
```bash
sudo useradd username
```

### `adduser` — Add New User (Interactive)
```bash
sudo adduser username
```

---

## Deleting Users

### `userdel` — Delete User
```bash
sudo userdel username
```

### `userdel` with Home Directory — Delete User and Home Directory
```bash
sudo userdel -r username
```

---

## Modifying Users

### `usermod` — Modify User Account
```bash
sudo usermod options username
```

### Change User's Shell
```bash
sudo usermod -s /path/to/shell username
```

### Change User's Home Directory
```bash
sudo usermod -d /new/home/dir username
```

---

## User Groups

### `groupadd` — Add New Group
```bash
sudo groupadd groupname
```

### `groupdel` — Delete Group
```bash
sudo groupdel groupname
```

### `usermod` — Add User to Group
```bash
sudo usermod -aG groupname username
```

### `groups` — List Groups for User
```bash
groups username
```

---

## Password Management

### `passwd` — Change Password
```bash
passwd username
```

### Lock and Unlock User Accounts
```bash
sudo passwd -l username  # Lock
sudo passwd -u username  # Unlock
```

---

## Switching Users

### `su` — Switch User
```bash
su username
```

### `sudo` — Execute Command as Other User
```bash
sudo -u username command
```

---

## User Information

### `id` — Display User and Group IDs
```bash
id username
```

### `who` — Who is Logged In
```bash
who
```

### `w` — Detailed Who is Logged In
```bash
w
```

### `last` — Last Logins
```bash
last
```

---
