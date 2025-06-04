---
title: "How I Add Citations in Obsidian: Manual to Fully Automated"
permalink: obsidian-reference
date: 2025-06-04
excerpt: Let me walk you through three ways—starting from the simplest to the most powerful automation I use every day to  add Citations in Obsidian
type: Blog
categories: 
tags: 
status:
---

If you're using Obsidian for research, notes, or writing papers, adding citations becomes essential. I often get asked:

> **“How do you manage citations in markdown inside Obsidian?”**
> ***"How to do you add citations in the markdown file"***
> ***How to add reference in obsidian notes?***
> ***What is the automated way to add reference or citation in obsidian?***

Let me walk you through three ways—starting from the simplest to the most powerful automation I use every day to  add Citations in Obsidian (Simple + Automated Ways)

---
## ✅ Method 1: Manual Footnote Citation

This is the most basic method. It works for short notes or quick references.

### Step-by-step:

1. At the point where you want to cite, add:
    ```
    This idea was inspired by Smith et al. ^[1]
    ```
2. Then, at the bottom of the note (or under a `## References` heading), add:
    ```markdown
    [^1]: Smith, J. (2020). *Understanding AI*. AI Press.
    ```
It’s simple but can get repetitive if you cite frequently.

---

## ⚙️ Method 2: Fully Automated Citations Using Zotero + Plugin

If you deal with a lot of PDFs and academic papers, **Zotero is a must-have**.
### What I Do:
1. **Store PDFs in Zotero**  
    I organize all my research papers in Zotero. It manages metadata, tags, and more.
2. **Use the Obsidian Zotero Integration**
    - I use the  the [Citations Plugin](https://github.com/hans/obsidian-citation-plugin).
    - Set up a BibTeX export from Zotero into Obsidian folder
    - Refer the BibTex to Citations Plugin
3. **Insert Citations with a Shortcut**  
    Once the plugin is configured, I can just type my predefined shortcut and pick the paper I want. It automatically generates citations and bibliography for me.
    
I even made a video showing the setup process:  

<iframe width="560" height="315" 
    src="https://www.youtube.com/embed/sERXPJAT5KA" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen>
</iframe>

After setup, it feels like magic. I can reference any of my 500+ papers in seconds—no copy-pasting required.

---

## 🔁 Method 3: Semi-Automated Footnote with Shortcut

This bridges the gap between manual and fully automated.
### How It Works:
- I use the **Footnote Shortcut Plugin** in Obsidian.
- I configure a hotkey so when I press it, it creates a footnote block automatically.
- I then paste the reference inside.
It’s faster than manual, and works well when you don’t use Zotero or just want quick footnote-style citations.
---
## Final Thoughts
There’s no “one right way”—it depends on your workflow.  
But if you're doing academic writing or managing lots of references:

> **Go for Zotero + Plugin**. It saves hours over time.

If you're writing casual notes or blog posts, the footnote method works just fine.

---
Let me know if you want a tutorial on setting up Zotero or Obsidian plugins. I’d be happy to share more.

---
Shuvangkar Das, PhD
Knoxville, Tennessee, USA
### ☎ Connect with me
- Twitter: [https://twitter.com/shuvangkar_das](https://twitter.com/shuvangkar_das)
- LinkedIn: [https://www.linkedin.com/in/ShuvangkarDas/](https://www.linkedin.com/in/ShuvangkarDas/)
- YouTube: [https://www.youtube.com/ShuvangkarDas](https://www.youtube.com/ShuvangkarDas)

### 📚References




