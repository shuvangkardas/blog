---
title: "Automated Task Management System in Obsidian (EP 1)"
permalink: /automated-obsidian-task-management-system/
date: 2026-02-11
excerpt: "Learn how to build an automated task management system in Obsidian that pulls urgent tasks, today's focus, weekly goals, and overdue reminders automatically."
type: Blog
categories:
- Productivity
- Knowledge Management
tags:
- Obsidian
- task management
- automation
- daily note
- productivity
- Obsidian starter kit
status: published
---

Every morning the first thing I open isn't email—it's Obsidian. And waiting for me there is my daily dashboard. It tells me what to do, what is urgent, what is the focus today and what is the focus of this week and it also tells me what I shouldn't waste time on.

But the problem is that my knowledge vault has grown to over 6,400 notes. I have tasks scattered across projects, meeting notes, and random ideas. I used to waste time every morning deciding what to work on, missing deadlines, and feeling overwhelmed by the sheer volume of information. The #1 pain point I faced was: how do I surface only the relevant tasks and priorities from thousands of notes without manually copying them each day?

If you've ever felt lost in your own notes, not knowing what to focus on today, you're not alone. This is the exact struggle that led me to build a system that automatically curates my daily dashboard.

## What You'll Get From This

By following this tutorial, you'll learn how to:
- Set up Obsidian's Daily Notes plugin to create a new daily note every morning
- Configure a template that automatically pulls in tasks from across your vault
- Use the Task plugin to filter overdue tasks, weekly goals, and daily priorities
- Build a dashboard that updates itself—no manual copying required
- Customize the system to match your workflow and preferences

## The Solution: Building Your Automated Daily Dashboard

### Step 1: Install the Obsidian Starter Kit (Optional but Recommended)

The easiest way to follow along is to download my free Obsidian Starter Kit. It comes pre‑configured with the folder structure, templates, and plugin settings you’ll need. You can find the link in the description below.

After downloading and unzipping, open the vault. You’ll see a folder structure like this:

- `Home/` – your personal notes
- `Work/` – professional documents
- `Projects/` – ongoing work
- `Journal/` – where daily notes will live

### Step 2: Enable the Daily Notes Plugin

Go to **Settings → Community Plugins** and enable the **Daily Notes** plugin. This plugin is built into Obsidian and is the foundation of our system.

Once enabled, configure the daily note location:
- Set the **Daily note folder** to `Journal/Daily Notes/` (or any folder you prefer)
- Set the **Template file location** to `Templates/Daily Note Template.md` (we’ll create this next)
- Enable **Open daily note on startup** so Obsidian shows your dashboard every morning

### Step 3: Create the Daily Note Template

Create a new note in your template folder called `Daily Note Template.md`. Inside, add the following YAML front matter and structure:

```yaml
---
date: {{date}}
---

## Today's Tasks

## Daily Journal

## Notes
```

The `{{date}}` placeholder will be replaced with today's date when the template is used.

### Step 4: Configure the Task Plugin

Install the **Task** community plugin. This plugin allows you to query tasks from across your vault based on due dates, tags, and other criteria.

In your daily note template, add a task query that pulls all tasks due today:

```markdown
## Today's Tasks
{{query: not done AND due today}}
```

You can also add queries for overdue tasks, weekly tasks, and upcoming deadlines.

### Step 5: Curate Tasks from Multiple Projects

The real power comes when you start tagging tasks in your project notes. For example, in a project note for "DustPlotter" you might add:

```markdown
- [ ] #task Integrate new feature into Python version :: due 2026-02-11
```

When you open your daily note, the Task plugin will automatically pull that task into the "Today's Tasks" section. No manual copying needed.

### Step 6: Customize and Beautify

The Task plugin offers advanced filtering options. You can sort tasks by priority, group them by project, or hide completed tasks. Explore the plugin's documentation to tailor the system to your needs.

Remember: the goal isn't to have a perfect system on day one. Start simple, then iterate as you discover what works for you.

## Watch the Full Video

For the complete step-by-step walkthrough, watch the full video below:

<iframe width="560" height="315" src="https://www.youtube.com/embed/jKDnXnuC-8Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

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