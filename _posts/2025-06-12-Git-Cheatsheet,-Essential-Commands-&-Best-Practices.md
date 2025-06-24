---
title: Git Cheatsheet, Essential Commands & Best Practices
permalink: git-cheatsheet
date: 2025-06-12
excerpt: 
type: Blog
categories: 
tags: 
status:
---
Managing code efficiently is essential in any software project. Git, a powerful distributed version control system, provides the foundation for version control and collaboration. This cheatsheet lists the **most essential Git commands and workflows** that every developer should know, from initializing a repository to recovering lost work.

---
## Git for Absolute Beginners

If you are complete beginner, I would suggest to start using following three commands. These are the commands you need most of the time.

- `git init` – Start a new Git repository in your folder.
- `git add .` – Stage all changes in the current folder.
- `git commit -m "message"` – Save the staged changes with a message.

**Simple Analogy**  
Think of `git add` as collecting all your notes into a folder.  `git commit` is photocopying that folder and storing it with a label — a version you can always come back to.

To check what’s going on at any point:
- `git status` – Shows current file changes and stage status.

### Connect to GitHub

1. First, create a repository on GitHub.  
2. Then run:

- `git remote add origin <repo-url>` – Connects your local repo to GitHub.
- `git branch -M main` – Rename local branch to `main` (used by GitHub).
- `git push -u origin main` – Push for the first time and set upstream.

Next time, just use:
- `git push` – Push new commits to GitHub.
- `git pull` – Pull changes from GitHub to your local repo.

> 🔒 First push may ask for login. Use your GitHub credentials

---
## 🔧 Basic Git Commands

These are the fundamental Git commands used daily in project management:
- `git init` – Initialize a new Git repository in the current directory.
- `git clone [url]` – Clone a remote repository to your local machine.
- `git status` – View the current status of your working directory and staging area.
- `git log` – View the commit history.
- `git add file1.c` – Stage changes in a specific file.
- `git add dir1/` – Stage all changes within a folder.
- `git add .` – Stage all changes in the current directory and subdirectories.
- `git add -A` – Stage all changes across the entire project, including deletions.
- `git commit -m "commit message"` – Commit staged changes with a message.
- `git push -u origin <branch>` – Push a new branch to remote and set upstream (first time).
- `git push` – Push the current branch to its upstream.
- `git pull` – Fetch and integrate changes from the remote repository.

---

## 🚀 Publishing a Release

To publish a version of your project, use Git tags:
- `git tag v0.1.0` – Create a lightweight tag.
- `git tag -a v0.5 -m "Release version 0.5"` – Create an annotated tag.
- `git push origin <tag_name>` – Push a tag to the remote repository.

---

## 🛠️ Resetting Changes

Git offers flexible options for undoing commits:

- `git reset --soft HEAD~1` – Undo last commit but keep changes staged.
- `git reset --hard HEAD~1` – Undo last commit and discard changes.
- `git reset <file>` – Unstage a file without modifying its contents.

---

## 🌐 Remote Repository Management

- `git remote -v` – View current remote URLs.
- `git remote set-url origin <new_url>` – Change the remote origin URL.

---

## 🚫 Ignore Tracked Files

To stop tracking files already committed (even if they're now in `.gitignore`):
- `git rm --cached <file>` – Remove file from Git index (keeps it locally).
- `git rm -r --cached <folder>` – Remove a folder from Git index.

📝 _This is especially useful for removing large files accidentally committed._

---

## 🤝 Collaborating on GitHub

### Access Control

- Only lead developers have write access to the main repository.
- Others work via forked copies of the repository.

### Forking

- Create a personal copy of the repository under your account.
- Make changes freely without affecting the main repo.

### Pull Requests

- Propose changes by [creating a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests).
- The core team will review and merge or reject your proposal.

### Branch Naming Convention

- Use date-prefixed branch names like: `2023JAN01_FeatureBranch`.
    

---

## 🔀 Managing Branches

- `git checkout -b <branch-name>` – Create and switch to a new branch.
- `git checkout main` – Switch to main (or any) branch.
- `git merge <branch>` – Merge another branch into the current one.

📝 _Make sure to be on the destination branch before merging._

---

## 🧨 Resolving Merge Conflicts with Binary Files

Binary files can't be merged automatically. Use:

```bash
git checkout --ours -- path/to/file.txt
git checkout --theirs -- path/to/file.txt
```

Or use:

```bash
git mergetool
```

Git opens three files:

- `{conflicted}.HEAD` (your version),
- `{conflicted}.REMOTE` (incoming),
- `{conflicted}` (working copy).

Manually resolve by copying contents as needed, then close the editor.

---

## 🛡 Fixing SSL Certificate Issues on Windows

Facing "unable to get local issuer certificate" in Git for Windows?

```bash
git config --global http.sslbackend schannel
```

This configures Git to use Windows’ certificate store instead of OpenSSL.

---

## 🕵️‍♂️ Recovering Lost Work in Git

If you lose files due to a hard reset or accidental delete, try:
1. **View the Reflog**
    ```bash
    git reflog
    ```
See recent commits and actions.
2. **Identify the Commit**
    - Look for the commit before the loss occurred.    
3. **Restore the Commit**
    ```bash
    git checkout <commit-hash>
    ```
Access the state of the repo at that commit and recover your work.
    


### 👋 About Me
Hi, I’m **Shuvangkar Das**, a power systems researcher with a Ph.D. in Electrical Engineering from Clarkson University. I work at the intersection of power electronics, DER, IBR, and AI — building greener, smarter, and more stable grids. Currently, I’m a Research Scientist at EPRI (though everything I share here reflects my personal experience, not my employer’s views).

Over the years, I’ve worked on real-world projects involving large scale EMT simulation and firmware development for  grid-forming and grid following inverter and reinforcement learning (RL). I also publish technical content and share hands-on insights with the goal of making complex ideas accessible to engineers and researchers.

📺 Subscribe to my [YouTube channel](https://www.youtube.com/@ShuvangkarDas), where I share tutorials, code walk-throughs, and research productivity tips.

<p><strong>Connect with me:<br></strong>
<a href="https://www.youtube.com/@ShuvangkarDas" target="_blank">
    <img src="https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube">
  </a>
  <a href="https://www.linkedin.com/in/ShuvangkarDas" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin">
  </a>
  <a href="https://newsletter.shuvangkardas.com" target="_blank">
    <img src="https://img.shields.io/badge/Newsletter-Subscribe-blue?style=for-the-badge">
  </a>
  <a href="https://twitter.com/shuvangkar_das" target="_blank">
    <img src="https://img.shields.io/badge/Twitter-Follow-blue?style=for-the-badge&logo=twitter">
  </a>
  
  <a href="https://github.com/shuvangkardas" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github">
  </a>
  <a href="https://blog.shuvangkardas.com" target="_blank">
    <img src="https://img.shields.io/badge/Blog-Read-blueviolet?style=for-the-badge">
  </a>
  
</p>

### 📚References
- [Git Official Guides](https://github.com/git-guides/)
- [Shuvangkar Das on GitHub](https://github.com/shuvangkar)
- [[Git Basic Command Cheatsheet]]



