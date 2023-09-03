# Git Commands Cheatsheet

A comprehensive guide to essential Git commands for version control.

## Table of Contents
1. [Introduction](#introduction)
2. [Setup and Configuration](#setup-and-configuration)
3. [Local Repository](#local-repository)
4. [Remote Repository](#remote-repository)
5. [Branching](#branching)
6. [Merging and Rebasing](#merging-and-rebasing)
7. [Stashing and Cleaning](#stashing-and-cleaning)
8. [Logging](#logging)
9. [Aliases](#aliases)
10. [Advanced](#advanced)

---

## Introduction

This cheatsheet aims to provide a quick reference for frequently used Git commands.

---

## Setup and Configuration

### `git config` — Configuring Git
```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

### `git config` — Listing Configuration
```bash
git config --list
```

---

## Local Repository

### `git init` — Initialize Local Repository
```bash
git init
```

### `git clone` — Clone Repository
```bash
git clone <repository-url>
```

### `git add` — Add Files to Stage
```bash
git add .
git add <file-name>
```

### `git commit` — Commit Changes
```bash
git commit -m "Commit message"
```

### `git status` — Check Status
```bash
git status
```

---

## Remote Repository

### `git remote` — Add Remote Repository
```bash
git remote add origin <repository-url>
```

### `git push` — Push to Remote Repository
```bash
git push origin master
```

### `git pull` — Pull from Remote Repository
```bash
git pull origin master
```

### `git fetch` — Fetch from Remote Repository
```bash
git fetch origin
```

---

## Branching

### `git branch` — Create Branch
```bash
git branch <branch-name>
```

### `git checkout` — Switch Branch
```bash
git checkout <branch-name>
```

### `git branch -d` — Delete Branch
```bash
git branch -d <branch-name>
```

### `git branch` — List Branches
```bash
git branch
```

---

## Merging and Rebasing

### `git merge` — Merge Branches
```bash
git merge <branch-name>
```

### `git rebase` — Rebase Branch
```bash
git rebase <branch-name>
```

---

## Stashing and Cleaning

### `git stash` — Stash Changes
```bash
git stash
```

### `git stash apply` — Apply Stashed Changes
```bash
git stash apply
```

### `git clean` — Clean Untracked Files
```bash
git clean -fd
```

---

## Logging

### `git log` — View Commit History
```bash
git log
```

### `git log --oneline` — View Commit History (Simple)
```bash
git log --oneline
```

---

## Aliases

### Setting an Alias
```bash
git config --global alias.<alias-name> '<git-command>'
```

---

## Advanced

### `git reset` — Reset to Previous Commit
```bash
git reset <commit-hash>
```

### `git revert` — Revert a Commit
```bash
git revert <commit-hash>
```

### `git bisect` — Binary Search to Find Bugs
```bash
git bisect start
git bisect bad
git bisect good <commit-hash>
```

---
