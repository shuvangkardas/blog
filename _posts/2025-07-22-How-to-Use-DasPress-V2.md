---
title: Turn Your Obsidian Notes into Blogs in 1 Click — Here’s How
permalink: obsidian-to-blog-v2-user-guide
date: 2025-07-22
excerpt: You’ve written hundreds of notes in Obsidian... but how many of them actually made it to your blog? If you’ve ever felt overwhelmed by the friction of converting, formatting, pushing to internet, or just getting started, you’re not alone. That’s exactly why I built DasPress.With one click, I now publish beautifully formatted blog posts straight from my Obsidian vault. No manual copy-pasting, no image chaos, no terminal gymnastics. In this guide, I’ll show you the exact setup I use,  so you can spend more time writing and less time wrestling with your publishing workflow.
type: Blog
categories: 
tags: 
status:
---
>**Note:** This documentation applies to **DasPress v2.0** only.  
>DasPress is actively evolving — check the [official site](https://shuvangkardas.com/daspress) for the latest updates and features.
## Table of Contents
1. [What is DasPress?](#what-is-daspress)
2. [Install and Configure DasPress (From Source)](#install-and-configure-daspress-from-source)
3. [Configure DasPress (One-Time Setup)](#-configure-daspress-one-time-setup)
4. [Connect DasPress to Obsidian](#-connect-daspress-to-obsidian)
5. [Using DasPress Inside Obsidian](#using-daspress-inside-obsidian)
6. [Example Workflow](#-example-workflow)
7. [Troubleshooting](#-troubleshooting)
8. [Updating & Uninstalling](#-updating--uninstalling)
9. [Final Tips](#-final-tips)

# What is DasPress?

Welcome to the official documentation for **DasPress v2.0**, a one-click publishing tool that converts your **Obsidian notes** into fully formatted **Jekyll blog posts**. It’s designed to:
- Eliminate friction in the writing-to-publishing workflow
- Help you build a consistent writing habit
- Boost productivity with minimal configuration

**DasPress is built for:**
- 💤 Anyone who avoids publishing due to setup hassles
- 💻 Power users willing to configure once and publish with one click
- ✨ Bloggers seeking a seamless publishing workflow

This manual walks you through installation, configuration, and usage from [source](https://github.com/shuvangkardas/daspress).
# Install and Configure DasPress (From Source)
DasPress is a Python-based tool and can be installed using `pip`.

### Step 1: Install Python
Download and install the latest version of Python:
🔗 [https://www.python.org/downloads/](https://www.python.org/downloads/)

Make sure to check the box **“Add Python to PATH”** during installation.
### Step 2: Verify Python Installation
Open a command prompt and run:
```bash
python --version
# or
python3 --version
```
![Pasted image 20250722052434.png](/assets/images/Pasted-image-20250722052434.png)
### Step 3: Install DasPress via pip
In a fresh terminal, run:

```bash
pip install daspress
```
![Pasted image 20250722052448.png](/assets/images/Pasted-image-20250722052448.png)
### Step 4: Verify DasPress Installation
Confirm the installation with:
```bash
python -m daspress --version
```
![Pasted image 20250722052538.png](/assets/images/Pasted-image-20250722052538.png)

## 🛠 Configure DasPress (One-Time Setup)
This step ensures DasPress knows where your blog folders and assets live.
![Pasted image 20250722052729.png](/assets/images/Pasted-image-20250722052729.png)
### ✅ You’ll need four folder paths:
1. **Obsidian Blog Folder**
   This is where your blog markdown files are stored.
2. **Image Attachment Folder (Inside Obsidian)**
   Typically a subfolder like `attachments/` under your blog folder.
3. **Jekyll Blog Post Directory**
   For GitHub Pages, this is usually the `_posts/` folder.
4. **Jekyll Blog Image Directory**
   Where images go in your blog repository (e.g., `assets/img`).

### Step 5: Run DasPress Setup
In your terminal:
```bash
python -m daspress setup
```
This will prompt you to enter the above folder locations. They’ll be saved for future use.
![Pasted image 20250722052814.png](/assets/images/Pasted-image-20250722052814.png)
### Step 6: Confirm Setup
After setup, navigate to your user directory:
```bash
~/.daspress/config.json
```

You should see your saved configuration.
![Pasted image 20250722053018.png](/assets/images/Pasted-image-20250722053018.png)
Congratulations! Configuration is complete. Now it's time to boost your productivity.


## 🔗 Connect DasPress to Obsidian

DasPress works through the **command line**, so we’ll connect it to Obsidian using a plugin.

### Prerequisites
* You have a working **GitHub Pages** or **Jekyll** blog setup on your machine.
* You can push to your remote GitHub repo.

### Step 1: Install Required Obsidian Plugins
1. **Shell Commands**
   Allows you to run terminal commands from Obsidian.
2. *(Optional)* **Commander Plugin**
   Lets you add buttons and shortcuts for commands.

### Step 2: Create Shell Command
Add a new command in Shell Commands:
```bash
python -m daspress remote "{{file_path:absolute}}"
```

![Pasted image 20250722053432.png](/assets/images/Pasted-image-20250722053432.png)
This command is instructing Obsidian to run DasPress and  pass the current file absolute path to it.
Also this command doing multiple steps, converting your blog, then pasting into your Jekyll site then doing all of the git push stuffs.  
   
Currently, Obsidian support four commands. You can experiment others as well. I normally start with convert (replace remote with convert) command to make sure DasPress is working. Then go with `remote` command

You can replace `convert` with any of the following supported commands:

| Command   | Description                                                        |
| --------- | ------------------------------------------------------------------ |
| `convert` | Convert note to blog post (Jekyll format only)                     |
| `local`   | Convert + Preview in local Jekyll server (Need Jekyll local setup) |
| `remote`  | Convert + Push to remote GitHub repo                               |
| `both`    | Convert + Preview + Publish                                        |

## Using DasPress Inside Obsidian
Once Shell Command is set up, you can publish blogs in three ways:

### 🔘 Method 1: Button (Recommended)
* Use the **Commander Plugin** to create a toolbar button.
* Link it to your DasPress command (e.g., `remote` or `both`).
* Clicking the button will publish your blog post.

### 🎛 Method 2: Command Palette
* Open Obsidian's Command Palette (`Ctrl+P`)
* Search for your custom shell command
* Run it manually

### 🎹 Method 3: Keyboard Shortcut
* Go to `Settings > Hotkeys`
* Search for “Shell Command”
* Assign your preferred hotkey

Now you can publish your blog with just one click or keystroke 🚀

## 🧪 Example Workflow
Normally I go with button at the top right.  **I used commander plugin to configure the button.**
![Pasted image 20250722053912.png](/assets/images/Pasted-image-20250722053912.png)

Finally when my blog is ready, I click the button and bam! my blog is online. 
![Pasted image 20250722053931.png](/assets/images/Pasted-image-20250722053931.png)


## 🧰 Troubleshooting

### `ModuleNotFoundError: No module named 'daspress'`

* Reinstall with `pip install daspress`
* Confirm the environment 

### Command not recognized (`python` or `daspress`)
* Add Python to your system PATH
* Try `python3` instead of `python`

### Obsidian shell command not working?
* Use the full path to your Python executable
* Ensure plugin permissions are enabled

---
## 🔄 Updating & Uninstalling

To update:
```bash
pip install --upgrade daspress
```

To uninstall:
```bash
pip uninstall daspress
```

---

## 📌 Final Tips

* Want automatic blog deployment? Use `remote` or `both` commands.
* Need Markdown cleanup or formatting options? Check the [DasPress GitHub](https://github.com/shuvangkar/daspress) for advanced settings.
* Prefer no-code? Use the [portable app](https://shuvangkardas.com/daspress/).


---

**Real stories. Practical lessons. Right in your inbox.**  
No spam—just once a week.  
{% include newsletter.html %}

---
### 👋 About Me
Hi, I’m **Shuvangkar Das** — a power systems researcher with a Ph.D. in Electrical Engineering, currently working as a Research Scientist. I work at the intersection of power electronics, inverter-based DERs (IBRs), and AI to help build smarter, greener, and more stable electric grids. 

My work spans large-scale EMT simulations, firmware development, reinforcement learning, and hardware prototyping. Beyond engineering, I’m also a [YouTuber](https://www.youtube.com/@ShuvangkarDas) and content creator — sharing hands-on insights on productivity, research, and knowledge management. My goal is simple: to make complex ideas more accessible and actionable for everyone.

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

### 📚 Obsidian Notes I Used for This Blog
[[How to Use DasPress V2.0.0]]


