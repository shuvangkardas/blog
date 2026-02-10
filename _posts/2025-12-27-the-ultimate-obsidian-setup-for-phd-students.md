---
permalink: the-ultimate-obsidian-setup-for-phd-students
categories:
    - Productivity
    - Research
    - Academia
tags:
    - obsidian
    - phd
    - research
    - literature-review
    - second-brain
    - academic-writing
---

Research is hard and difficult. I always acknowledge that. But there is a way to make it frictionless and easy to maintain — using Obsidian as your note-taking system and managing your research project inside Obsidian.

In this guide, I'll show you **five Obsidian plugins and settings** that transform your research workflow and build your research second brain.

## Why Obsidian for Research?

As a PhD student or academic researcher, you juggle:
- Reading papers and taking notes
- Managing literature reviews
- Tracking meetings with supervisors
- Organizing experiments and data
- Maintaining research logs
- Managing deadlines and tasks

Instead of jumping between multiple tools, you can manage your **entire research project inside Obsidian**.

---

## Step 1: Setting Up Your Research Hub

### Download and Install Obsidian
Visit [obsidian.md](https://obsidian.md) and download Obsidian for your platform.

### Understanding "Vaults"
When you first open Obsidian, you'll see three options:
1. Create a new vault
2. Open folder as vault
3. Open vault from Obsidian Sync

**Important:** A "vault" is just Obsidian's terminology for a folder. That's it — simple as that.

### Creating Your Research Hub
1. Click **Create new vault**
2. Name it something like "Research Hub"
3. **Crucially**, select a location that's backed up automatically (like OneDrive, Google Drive, or Dropbox)

> 💡 **Pro Tip:** Since you're building a knowledge base for your entire research career, store it in a cloud-synced folder from day one.

---

## 5 Essential Plugins for Research Workflow

### 1️⃣ PDF++ (Literature Review Plugin)

PDF++ is a **game-changer** for researchers. It allows you to:

- **Highlight PDFs directly inside Obsidian**
- **Convert paper highlights into notes** with bidirectional linking
- **Jump from note → exact PDF location** instantly
- **Track where every quote came from** (essential for citations)

**How it works:**
1. Install PDF++ from Community Plugins
2. Open a PDF in Obsidian
3. Select text and use "Copy with callout" to create a linked note
4. When your supervisor asks "Where did you get this line?", click and the PDF opens at that exact location

> 🔗 **Deep dive:** [PDF++ Plugin Video](https://youtu.be/R8H4sY5y8kQ?si=vdlhfb6EMQZUHaCu)

### 2️⃣ Templates Plugin

Templates allow you to **replicate consistent formatting** across your research notes.

**What you can create:**
- Research logs
- Meeting notes with supervisors
- Literature review templates
- Daily research journals
- Experiment tracking notes

**Setup:**
1. Enable the Templates core plugin
2. Create a "Templates" folder
3. Create templates with YAML front matter:
   ```yaml
   ---
   title: {{title}}
   date: {{date}}
   tags: [log]
   ---
   ```

**Usage:** Insert templates with one click to populate headers, dates, tags, and structure automatically.

### 3️⃣ Natural Language Dates

This plugin makes timestamping **effortless and consistent**.

**Features:**
- Type `@today` to insert today's date
- Type `@tomorrow` for tomorrow's date
- Type `@2026-01-02` for any date
- Automatically creates linked notes for dates

**Use cases:**
- Research journal entries
- Meeting notes with supervisors
- Experiment logs
- Project milestones

> 📅 Perfect for keeping track of **when** things happened — essential for research documentation.

### 4️⃣ Tasks Plugin (Research Task Management)

Transform your meeting notes into **actionable tasks**.

**How it works:**
1. In any note, create a task:
   ```markdown
   - [ ] Submit project report #task due:today
   - [ ] Complete experiment #task due:tomorrow
   ```
2. Tasks automatically appear in your task manager
3. Set due dates directly in notes

**Integration with Daily Notes:**
Create a task code block to collect all tasks from your vault:
````
```tasks
not done
due today
```
````

> 🎯 **Pro tip:** Use daily notes as your research control center to see all tasks in one place.

### 5️⃣ Daily Notes (Your Research Control Center)

Daily Notes is a core plugin that **automatically creates a new note each day**.

**Why it's essential:**
- Creates a daily research journal automatically
- Collects all tasks from your vault
- Plans your research day in one place
- Tracks experiments, meetings, and ideas over time

**Setup:**
1. Enable Daily Notes core plugin
2. Configure date format
3. Open "Today's daily note" anytime

**Workflow:**
- Each morning: Review your daily note
- During the day: Log tasks and notes
- Each evening: Plan tomorrow's research goals

---

## Putting It All Together: Your Research Second Brain

Here's how these plugins work together to create a frictionless research system:

### Daily Workflow:
1. **Morning:** Open Obsidian → Daily note shows tasks + schedule
2. **Literature Review:** Use PDF++ to read papers and create linked notes
3. **Meetings:** Use Templates + Natural Language Dates for meeting notes
4. **Task Tracking:** Create tasks in notes, see them all in Daily Notes
5. **Evening:** Log research progress, plan tomorrow's tasks

### Long-term Benefits:
- ✅ **Never lose a reference** — everything is linked and searchable
- ✅ **Instant citation tracking** — jump from note to paper location
- ✅ **Reduced mental load** — one system, not five tools
- ✅ **Research documentation** — dates and context preserved
- ✅ **Long-term knowledge base** — build your research second brain

---

## Who Is This For?

- **PhD students** managing literature reviews and experiments
- **Academic researchers** juggling multiple projects
- **Graduate students** learning research workflows
- **Research engineers** building knowledge systems
- **Knowledge workers** managing complex projects

If you do **research, writing, or long-term thinking**, this workflow will help.

---

## Resources Mentioned

- **Obsidian Download:** [obsidian.md](https://obsidian.md)
- **Obsidian Starter Playlist:** [Watch here](https://www.youtube.com/watch?v=fK2ZYKi7tBE&list=PLTmvRP1LI8sX1rMYcIQuiXhwevL6Q1P1t)
- **PDF++ Deep Dive:** [Video tutorial](https://youtu.be/R8H4sY5y8kQ?si=vdlhfb6EMQZUHaCu)
- **Tasks Plugin Tutorial:** [Part 1](https://youtu.be/jKDnXnuC-8Y?si=m2O_sIjiSThgBQjE) | [Part 2](https://youtu.be/8nXlATtXCfc?si=5NtbTI1xWeJC6Z5J)
- **Free Obsidian Starter Kit:** [shuvangkardas.com/obsidian-starter-kit](https://shuvangkardas.com/obsidian-starter-kit)

---

## Final Thoughts

Research doesn't have to be overwhelming. With the right setup in Obsidian, you can:

- **Stop losing references**
- **Answer "where did this come from?" instantly**
- **Track experiments, meetings, and ideas over time**
- **Reduce mental load**
- **Focus on thinking and writing, not tool-hopping**

This is how I build my **Research Second Brain** using Obsidian.

If you found this helpful, share it with fellow researchers! 👩‍🔬👨‍🔬

---

## SEO Keywords

Obsidian for research, Obsidian PhD workflow, literature review Obsidian, Obsidian PDF++, research second brain, Obsidian plugins for researchers, academic note taking, research project management, PhD productivity, Obsidian daily notes, Obsidian task management
