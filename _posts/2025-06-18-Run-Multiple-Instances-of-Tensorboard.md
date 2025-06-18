---
title: How I Run Multiple Tensorboard Instances to Compare Deep Learning Experiments Side by Side
permalink: run-multiple-tensorboard-instances
date: 2025-06-18
excerpt: Running multiple TensorBoard instances can be a game-changer when you're comparing models, tweaking hyperparameters, or just debugging deep learning pipelines. Here's how I run multiple logs in parallel using different ports — a simple trick that helped me speed up my workflow and make better training decisions.
type: Blog
categories: 
tags: 
status:
---

If you're deep into model training and experiment tracking like me, you've probably faced the need to monitor different runs side by side. At one point, I was juggling multiple folders of logs and manually switching directories, which felt clunky.

Eventually, I found a better way: **running multiple instances of TensorBoard** at the same time — each on a different port. This small change made my debugging and comparison process much more efficient.

Here’s how I do it.

---

## Step-by-Step: Run Multiple TensorBoard Instances

### ✅ Step 1: Open CMD in Your Project Folder

Make sure you’re inside the folder where your training script or log directory lives.

```bash
cd path/to/your/project
```

### ✅ Step 2: Activate Your Conda Environment

```bash
conda activate your_env_name
```

### ✅ Step 3: Launch TensorBoard

For the default log directory:

```bash
tensorboard --logdir=logs
```

Or to run on a specific port (e.g., 6007):

```bash
tensorboard --logdir=logs --port=6007
```

---

## Running Two TensorBoard Instances in Parallel

Let’s say you have two different training runs, each saving logs in different folders. Here’s what to do:

### 🖥️ Terminal Window 1:

```bash
tensorboard --logdir=path/to/first/logdir --port=6006
```

### 🖥️ Terminal Window 2:

```bash
tensorboard --logdir=path/to/second/logdir --port=6007
```

### Access in Browser:

- Visit `http://localhost:6006` for the first instance.
    
- Visit `http://localhost:6007` for the second instance.
    

---
## Why This Helped Me

When I was tuning hyperparameters for a reinforcement learning project, comparing reward curves across multiple runs in one interface just wasn’t cutting it. By running parallel TensorBoard instances, I could visually scan and compare experiments without jumping between folders or restarting logs.

---
## Final Thoughts

If you're training deep learning models regularly, learning how to run multiple TensorBoard sessions is a productivity boost. It's one of those small things that pay off big over time.


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




