# Filesystem Search Cheatsheet

A quick reference for searching within the filesystem on Unix-like operating systems.

## Table of Contents
1. [Introduction](#introduction)
2. [Find Command](#find-command)
3. [Locate Command](#locate-command)
4. [Grep Command](#grep-command)
5. [Additional Utilities](#additional-utilities)

---

## Introduction

Searching for files and directories is a common task. This cheatsheet provides an overview of some commonly used tools for filesystem searching, such as `find`, `locate`, and `grep`.

---

## Find Command

`find` is a powerful command for searching files in a directory hierarchy.

### Basic Search
```bash
find /path/to/search -name "filename"
```

### Search for Directories
```bash
find /path/to/search -type d -name "dirname"
```

### Search for Files
```bash
find /path/to/search -type f -name "filename"
```

### Case-Insensitive Search
```bash
find /path/to/search -iname "filename"
```

### Search with Wildcards
```bash
find /path/to/search -name "file*"
```

### Search by Size
```bash
find /path/to/search -size +1M
```

---

## Locate Command

`locate` is a faster method for searching the whole filesystem but might be less up-to-date.

### Basic Search
```bash
locate filename
```

### Case-Insensitive Search
```bash
locate -i filename
```

### Update Locate Database
```bash
sudo updatedb
```

---

## Grep Command

`grep` is a tool for searching inside files.

### Basic Search
```bash
grep "pattern" /path/to/file
```

### Case-Insensitive Search
```bash
grep -i "pattern" /path/to/file
```

### Recursive Search
```bash
grep -r "pattern" /path/to/search/
```

### Show Line Numbers
```bash
grep -n "pattern" /path/to/file
```

---

## Additional Utilities

### `which` — Locate a command
```bash
which command_name
```

### `whereis` — Locate binary, source, and manual pages
```bash
whereis command_name
```

### `type` — Describe a command
```bash
type command_name
```

---
