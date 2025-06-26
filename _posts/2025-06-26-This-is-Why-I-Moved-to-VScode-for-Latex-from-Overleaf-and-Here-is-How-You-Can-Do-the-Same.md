---
title: Why I Ditched Overleaf for VS Code--A Faster LaTeX Workflow for Writing Report and Manuscript
permalink: overleaf-local-alternative-latex-in-vscode
date: 2025-06-26
excerpt: Tired of Overleaf delays and manual uploads? Here’s how I transformed my LaTeX workflow using VS Code for faster compilation, Zotero integration, and Git control.
type: Blog
categories: 
tags: 
status:
---
At the beginning of my second year of PhD, my professor gave me a big task: prepare the final report for our project titled *"Real-Time Interconnection Studies and Control of New York Offshore Wind."*[^1]  This wasn’t a short summary — it was a hundred-page technical report. Like many others, I began using Overleaf, thinking it was the best choice for LaTeX documents. And initially, it was smooth. But as the report grew, the cracks began to show.

---

## Why Overleaf Didn't Work for Me

### 1. Slow Compilation with Large Documents  
As my report reached dozens of pages, every small edit triggered a long wait — sometimes several minutes — just to compile. When you're trying to focus, that delay is a productivity killer.

### 2. Attachment Management is a Pain  
Every time I tweaked a figure — even a small label — I had to re-upload the image manually into Overleaf. That might seem trivial, but in a hundred-page technical report, it quickly becomes frustrating and repetitive.

### 3. Manual Reference Upload from Zotero  
I use Zotero for all my paper management and citation tracking. My workflow involves adding new papers to a Zotero subfolder and generating a BibTeX file. But each time I added a paper, I had to upload the BibTeX file again into Overleaf. It broke the automation I wanted and made citation management unnecessarily manual.

### 4. Lack of Modern UI Features  
I prefer dark themes for long working hours, and Overleaf doesn’t support that. The interface feels outdated, lacks tab support, and isn’t optimized for writing large, modular reports.

### 5. No Free Git Integration  
Version control is crucial, especially when collaborating. But Overleaf charges for Git integration. For a student, that felt unnecessary — particularly when free alternatives exist.

---

## My Workflow Transformation with VS Code + LaTeX

After a frustrating experience, I began exploring local LaTeX editors. TeXStudio was my first try, but it didn’t feel modern or smooth. Then I discovered the power of **VS Code + LaTeX Workshop extension**. That completely changed my workflow and made everything 10x faster.

### 1. Instant Compilation  
Unlike Overleaf, compilation is blazing fast in VS Code — usually under a second. No more waiting to see changes.

### 2. Easy Figure Management  
All my figures are in a subfolder. When I update a figure, it automatically reflects in the report without any manual uploads. That’s peace of mind.

### 3. Fully Automated Zotero Integration  
I configured my Zotero subfolder to automatically export BibTeX into my manuscript folder. Now, when I add a paper to Zotero, it updates the `.bib` file without me touching anything. I just copy the cite key, and that’s it.

### 4. Customizable UI  
With VS Code, I use a dark theme, multiple tabs, and font settings optimized for writing. It’s far easier on my eyes, especially during long writing sessions.

### 5. Seamless Git and GitHub Integration  
Since everything is local, I manage my manuscript versions with Git. I push to GitHub and collaborate with co-authors without paying extra. I can even review commit history, create branches for different versions, and merge changes — all inside VS Code.

### 6. Peace of Mind  
No delays. No repeated uploads. No formatting glitches. Just writing, compiling, and focusing on content.

---

## How to Set Up LaTeX in VS Code[^2]

Here’s what I did to replicate this setup:
### Step-by-Step Installation  
1. **Install LaTeX Workshop Extension** in VS Code  
2. Download and install **[MiKTeX](https://miktex.org/)**  
3. Download and install **[Strawberry Perl](https://strawberryperl.com/)**  
4. Open your `.tex` file and press `Alt + Z` to enable **word wrap** — essential for readability

That’s it. You now have a powerful, offline LaTeX environment optimized for speed, automation, and version control.

---

If you're a researcher, grad student, or engineer writing long technical documents and struggling with Overleaf, give VS Code a shot. It saved me hours and gave me control back over my writing process.


---
### 👋 About Me
Hi, I’m **Shuvangkar Das**, a power systems researcher with a Ph.D. in Electrical Engineering from Clarkson University. I work at the intersection of power electronics, DER, IBR, and AI — building greener, smarter, and more stable grids. Currently, I’m a Research Engineer at EPRI (though everything I share here reflects my personal experience, not my employer’s views).

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

[^1]: https://www.nypa.gov/news/press-releases/2020/20201106-clarkson
[^2]: https://github.com/James-Yu/LaTeX-Workshop/wiki/Install
	[[Latex on vscode]]
