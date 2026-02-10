---
title: "How to Build a Folderless Note Taking System in Obsidian"
permalink: /folderless-note-taking-system-obsidian/
date: 2026-02-09
excerpt: "Learn how to build a sustainable folderless note taking system in Obsidian that you can maintain even when exhausted."
type: Blog
categories:
- Productivity
- Note-taking
tags:
- Obsidian
- note-taking
- folderless
- productivity
- knowledge management
- PKM
status: published
---

## Key Takeaways

- **Folderless systems reduce friction** — avoid nested folders and create linked notes for easier navigation.
- **Use index notes as hubs** — each major concern (home, study, work, etc.) gets an index note linked to its subnotes.
- **Decimal numbering organizes automatically** — prefix index notes with `00`, `10`, `20` for automatic sorting.
- **Master the Quick Switcher (Ctrl+O)** — jump to any note in seconds, even with thousands of notes.
- **Manage attachments separately** — set a dedicated attachment folder to keep your vault clean.
- **Think of your vault as a tree** — index notes are branches, individual notes are leaves, and a master note is the root.

## Introduction

Everyone starts note‑taking with high energy, but over time that energy fades. I’ve talked with ten high‑achieving people—PhD candidates and graduates—who all struggle to maintain an organized, folder‑based note‑taking system in Obsidian. The reason is simple: folders create friction. When you’re exhausted, the last thing you want is to navigate a maze of nested folders.

In this video, I build a system from scratch that is **folderless, easy to maintain, and sustainable even on your most tired days**. This blog post distills that workflow into a practical guide you can follow right now. If you’ve ever felt overwhelmed by your note‑taking system, this is your path to a cleaner, more intuitive setup.

## Setting Up Your Obsidian Vault for a Folderless System

The first step is to create a new vault. When you launch Obsidian, you’ll see three options: create new vault, open folder as a vault, and open vault from Obsidian Sync. Don’t be intimidated by the word “vault”—it’s just a folder where Obsidian stores all your notes.

For a folderless system, choose **Create new vault**. Name it something like “Thinking System” and select a location that syncs automatically (Google Drive, OneDrive, etc.). Syncing ensures you can access the same vault from any computer without paying for Obsidian Sync.

Once the vault is created, you’ll see the default interface: a file browser, a sample note, and a graph view. This is your blank canvas. The goal is to build a system where every note is **traceable**—no orphan notes left floating in the void.

### Why Folderless?

Traditional folder‑based systems force you to decide where a note belongs. Over time, the hierarchy becomes rigid and hard to navigate. A folderless approach uses **links** instead of folders. Each note is linked to a relevant index note, making it discoverable via search or the Quick Switcher.

## Creating Index Notes and Linking Your Notes

The core of a folderless system is the **index note**. These are hub notes that collect links to all related notes. In the video, the creator starts with ten main categories that cover every concern of life: Home, Study, Work, Hobby, Content, Business, Reserve (60), Reserve (70), Literature, and Archive.

Each category gets an index note prefixed with “mock” (meaning “map of content”). For example:

- `mock home` – all personal information (bio, finance, legal, credit cards, etc.)
- `mock study` – everything you learn (Python, C programming, etc.)
- `mock work` – projects, company wiki, meeting notes, etc.

### How to Create an Index Note

1. Create a new note (e.g., `mock home`).
2. Add a sub‑note under it (e.g., `bio`).
3. Link the sub‑note to the index note using double square brackets: `[[bio]]`.
4. Now the index note acts as a central hub—you can always find the `bio` note by going to `mock home`.

### Connecting All Index Notes with a Master Root

To tie all index notes together, create a **master note** (e.g., `mock master`). Link each category index note to it:

```
- [[00 mock home]]
- [[10 mock study]]
- [[20 mock work]]
- ...
```

This creates a tree structure: the master note is the root, the category notes are branches, and every other note is a leaf. In Obsidian’s graph view, you’ll see a beautiful tree of interconnected ideas.

## Using Decimal System and Quick Switcher for Navigation

When your vault grows to thousands of notes, finding the right index note can still be challenging. The solution is twofold:

### 1. Decimal Numbering for Automatic Sorting

Prefix each category index note with a two‑digit number (e.g., `00 mock home`, `10 mock study`, `20 mock work`). Obsidian sorts notes numerically, so all your index notes will appear at the top of the file list. This eliminates the need to scroll through hundreds of notes.

### 2. Master the Quick Switcher (Ctrl+O)

The Quick Switcher is Obsidian’s search‑based navigation tool. Press `Ctrl+O` (or `Cmd+O` on Mac) and start typing the name of any note. For example, typing “mock home” instantly filters to that index note. With thousands of notes, the Quick Switcher becomes your primary navigation method—fast, frictionless, and always available.

#### Pro Tip: Use “mock” as a Prefix

By prefixing all index notes with “mock,” you can type “mock” in the Quick Switcher and see every hub note at once. This works even if you don’t remember the exact name of the note you need.

## Managing Attachments and Growing Your Knowledge Tree

A common pitfall in note‑taking systems is attachment clutter: PDFs, images, and files scattered everywhere. Obsidian lets you control where attachments are stored.

### Setting Up an Attachment Folder

1. Open **Settings** → **Files & Links**.
2. Under **Default location for new attachments**, choose **In subfolder under current folder**.
3. Name the subfolder `Attachment` (or `attachments`).
4. Save.

Now, when you paste an image into a note, Obsidian automatically creates an `Attachment` folder and stores the image there. Your vault stays clean, and attachments are centralized.

### Thinking of Your Vault as a Tree

The speaker presents a powerful analogy: your vault is a living tree.

- **Root:** The master index note that connects everything.
- **Branches:** The category index notes (home, study, work, etc.).
- **Leaves:** Every individual note you create (bio, meeting notes, project ideas, etc.).

Every time you learn something new, you create a leaf. Every time you have a meeting, you create a leaf. Over time, your tree grows—both in breadth (more categories) and depth (more detailed notes). This mental model encourages you to link notes rather than orphan them, ensuring every leaf has a path back to the root.

## Conclusion / Final Thoughts

Building a folderless note‑taking system in Obsidian is about reducing friction and creating a sustainable habit. By using index notes as hubs, decimal numbering for order, and the Quick Switcher for navigation, you can maintain a vault of thousands of notes without feeling overwhelmed.

Start today: create a new vault, set up your ten categories, and link your first notes. You’ll be amazed at how quickly your knowledge tree grows—and how easy it becomes to find exactly what you need, even on your most exhausted days.

**Ready to see this system in action?** Watch the full video tutorial below for a step‑by‑step walkthrough.

---

**Real stories. Practical lessons. Right in your inbox.**  
No spam—just once a week.  
{% include newsletter.html %}

---

### 👋 About Me

Hi, I'm **Shuvangkar Das** — a power systems researcher with a Ph.D. in Electrical Engineering, currently working as a Research Scientist. I work at the intersection of power electronics, inverter-based DERs (IBRs), and AI to help build smarter, greener, and more stable electric grids. 

My work spans large-scale EMT simulations, firmware development, reinforcement learning, and hardware prototyping. Beyond engineering, I'm also a [YouTuber](https://www.youtube.com/@ShuvangkarDas) and content creator — sharing hands-on insights on productivity, research, and knowledge management. My goal is simple: to make complex ideas more accessible and actionable for everyone.

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