---
title: How I Resolve Git Conflicts in Simulink Models (Without Losing My Mind)
permalink: git-conflict-resolution-simulink-models
date: 2025-06-18
excerpt: If you're version-controlling Simulink models using Git, you’ve probably faced the frustration of binary file conflicts. In this post, I walk you through how I personally handle and resolve Simulink `.slx` file conflicts using Git—without relying on the built-in Simulink model browser.
type: Blog
categories: 
tags: 
status:
---

In one of my [previous tutorials]({% post_url 2025-06-09-How-Do-Git-Source-Control-of-Simulink-Project %}), I explained how to set up version control for Simulink models using Git. But let’s be honest—once binary files like `.slx` or `.mlx` are involved, merging conflicts becomes a real headache.

I’ve dealt with this many times, especially during collaborative development where multiple team members push changes to the same Simulink model. Simulink does offer a graphical model comparison and merge tool, but I often find it clunky and unreliable for real conflict resolution.

So here’s how I personally handle Git conflicts in Simulink models step by step:

---

## Handling Binary File Conflicts in Git for Simulink

When Git encounters a conflict in binary files, it can’t auto-merge them like it can with plain text. So you have to choose—whose version do you want to keep?

### 1. Identify the Conflicting File

In my case, the file Git flagged was:  
`Experimennt_RL/2024-07-28_PMSM_TD3/PMSM_TD3_Base/TrainTD3AgentForPMSMControlExample.mlx`

### 2. Choose Which Version to Keep

You typically have three choices:

- Keep **your local version**
    
- Accept **the remote version**
    
- Go back to **a specific commit**
    

### 3. Run Git Commands to Resolve the Conflict

**To keep your local version:**

```bash
git checkout --ours Experimennt_RL/2024-07-28_PMSM_TD3/PMSM_TD3_Base/TrainTD3AgentForPMSMControlExample.mlx
```

**To keep the remote version:**

```bash
git checkout --theirs Experimennt_RL/2024-07-28_PMSM_TD3/PMSM_TD3_Base/TrainTD3AgentForPMSMControlExample.mlx
```

**To go back to a previous commit version:**

First, find the commit hash:

```bash
git log Experimennt_RL/2024-07-28_PMSM_TD3/PMSM_TD3_Base/TrainTD3AgentForPMSMControlExample.mlx
```

Then check out the desired version:

```bash
git checkout [commit_hash] Experimennt_RL/2024-07-28_PMSM_TD3/PMSM_TD3_Base/TrainTD3AgentForPMSMControlExample.mlx
```

### 4. Mark the File as Resolved

Once you've decided which version to keep, run:

```bash
git add Experimennt_RL/2024-07-28_PMSM_TD3/PMSM_TD3_Base/TrainTD3AgentForPMSMControlExample.mlx
```

### 5. Complete the Merge

Now commit your changes:

```bash
git commit -m "Resolved binary file conflict in TrainTD3AgentForPMSMControlExample.mlx"
```

### 6. Push Your Final Changes

Finally, push your resolution to the remote branch:

```bash
git push origin master
```

---

In short, working with binary files in Git isn't ideal, but once you understand the workflow, you can resolve conflicts without panicking. Hope this helps anyone stuck resolving `.mlx` or `.slx` merge issues—been there too many times myself.


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
[[Git Manage Binary Files Conflict]]



