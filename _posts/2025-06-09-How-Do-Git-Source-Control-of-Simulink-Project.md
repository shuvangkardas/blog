---
title: Why Managing Simulink with Git Was a Nightmare, Until I Built This Workflow
permalink: how-to-manage-simulink-projects-with-git
date: 2025-06-09
excerpt: Struggling to collaborate on Simulink models using Git? After 5+ years of frustration, I built a bulletproof version control pipeline. Here’s how you can do it too—step-by-step.
type: Blog
categories: 
tags: 
status:
---
Let me take you to a familiar scene...

You’re working late on your Simulink model. After weeks of fine-tuning, you finally get it to simulate. Then your colleague sends you an “updated version” via email... and just like that, your version is overwritten, broken, or worst—gone.

I’ve been there. For the past 5–6 years, I worked on large-scale Simulink models, both during my PhD and now at EPRI. Every time a team project came up, version control was a pain. Emails flying back and forth, file conflicts, lost updates, corrupted `.slx` files—**Simulink just wasn’t built for Git workflows.**

But finally, after years of frustration and trial-and-error, I figured it out.

Today, I’m sharing the Git + Simulink workflow I wish I had learned years ago. It’s simple, reliable, and scalable. Whether you’re collaborating with one person or a whole team, this will change how you manage models forever.

> ⚠️ This tutorial assumes you already know the basics of Git source control.

---
### 🔧 Step 1: Open a Git Project from Simulink
- Go to **Simulink > Project > From Git**
- Enter the **remote repository path**
- Simulink will initialize the repo for you  
    ![Image](/assets/images/Pasted-image-20250609060519.png)

---
### 🧠 Step 2: Use a `.gitattributes` File (And Why It’s a Lifesaver)
By default, MATLAB adds this file in newer versions. But if it doesn’t, add one manually.
Here’s what it does:  
It tells Git how to handle Simulink binary files (`.slx`, `.mdl`, etc.) to avoid merge disasters.
Here’s a snippet I used in older versions:
```text
*.slx -crlf -diff -merge
*.mdl -crlf -diff -merge
*.mat -crlf -diff -merge
*.mlx -crlf -diff -merge
```

---

### 🔐 Step 3: Use GitHub Tokens for Authentication
GitHub no longer accepts passwords. Here’s the modern way:
- Go to **GitHub > Settings > Developer Settings > Personal Access Tokens**
- Generate a token and use it as your Git password when Simulink prompts

✅ Pro Tip: Give the token full access to “repo” scopes for smoother operations.

---
### 🚫 Step 4: Add a Clean `.gitignore` for Simulink
Avoid clutter and commit only the essentials. Here’s the `.gitignore` file I use:
```text
# Windows default autosave extension
*.asv

# OSX / *nix default autosave extension
*.m~

# Compiled MEX binaries (all platforms)
*.mex*

# Packaged app and toolbox files
*.mlappinstall
*.mltbx

# Generated helpsearch folders
helpsearch*/

# Simulink code generation folders
slprj/
sccprj/

# Matlab code generation folders
codegen/

# Simulink autosave extension
*.autosave

# Simulink cache files
*.slxc

# Octave session info
octave-workspace
```

---
### 💡 Step 5: Use Git Like a Pro (Yes, Even Inside MATLAB)
You can use Git in two ways:
- Directly in MATLAB’s terminal: prepend `!` before Git commands  
    _Example:_ `!git status`
- Or use your regular Git CLI or GUI (e.g., GitKraken, Sourcetree)

---
### 🎁 Bonus: Add Project Files to Git Properly
MATLAB’s default Git sometimes ignores subfolders or files.
To fix it:
- Go to the **Project** tab
- Click **Tools > Project Files > Add Files**
- Manually add folders or files you want to track  
    📸 _Insert screenshot here_

---
### Final Thoughts
I know the pain of collaborative modeling in Simulink. But with a structured Git pipeline, you don’t have to fear overwriting your files or emailing giant `.slx` files anymore. This guide is something I wish someone had shared with me years ago. Now, you can avoid those painful mistakes.

> Are you using Git with Simulink already? What tricks or problems have you run into?  
> Let me know in the comments or tag me on LinkedIn.

---
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
