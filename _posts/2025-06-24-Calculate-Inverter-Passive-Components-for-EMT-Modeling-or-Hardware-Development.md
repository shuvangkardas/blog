---
title: How I Design LC Filters for Inverters in EMT Simulations and Real Hardware
permalink: how-to-design-lc-filter-for-inverter-emt-simulation
date: 2025-06-24
excerpt: Designing LC filters for inverter-based systems is critical in both EMT simulations and hardware development. Here’s a practical, step-by-step guide based on my experience, including equations, assumptions, and key design principles.
type: Blog
categories: 
tags: 
status:
---
Over the last 10 years, I’ve spent a lot of time in power electronics—starting with my first inverter project in 2015. For the past three years, I’ve been working closely with EMT (Electromagnetic Transient) simulation tools to model inverter-based resources.

There’s one question that comes up often, whether you’re working in simulation or hardware:  
**How do you design the output LC filter of an inverter?**

It’s a small part of the overall system, but it has a big impact on performance. Getting it wrong can lead to high ripple, resonance, or even instability.

So, in this post, I’ll walk through the **exact steps** I follow to design the LC filter for inverters—useful for both **EMT modeling** and **real-world hardware development**.


### Define Parameters and Assumptions
Before doing any math, let's clarify a few things.
**Key Parameters:**
- Inverter switching frequency, $f_{sw}$
- DC link voltage, $V_{dc}$
- AC output voltage line to line, $V_{ac(LL)}$
- For simplicity let's consider output is purely resistive of load resistor, $R$
**Assumptions**
- Inductor current ripple, $\Delta i_{p p_{-} \max } = 20\%$
- Filter resonance frequency, $f_r = \frac{f_{sw}}{10}$ is standard practice to avoid interaction with switching frequency


### Step-by-Step LC Filter Design
1. Calculate peak current 
$$I_{peak} = \sqrt{2} \frac{V_{ac(LN)}}{R} = \sqrt{2} \frac{V_{ac(LL)}}{R\times \sqrt{3}}$$
2. Calculate maximum ripple current for 20% current ripple
$$\Delta i_{p p_{-} \max } = 0.2 \times I_{peak}$$
3. Calculate inductor value
$$
L=\frac{V_{dc}}{8 \Delta i_{p p_{-} \max } f_{s w}}
$$
4. Calculate filter resonance frequency, one tenth of switching frequency, to make sure filter does not resonate with switching frequency
$$\omega=\frac{2 \pi f_{s w}}{10}$$
5. Calculate capacitor value using the resonance frequency
$$C=\frac{1}{L \omega^2}$$

### Final Notes
This calculation assumes a purely resistive load and does **not include damping**, which is essential in many practical designs to control resonance peaking. I’ll cover damping resistor design and more advanced scenarios (like LCL filters) in future tutorials.

Whether you're designing for an EMT simulator or building a real inverter, getting your LC filter right is foundational—and this method has worked well for me across both domains.


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
[[GFM Calculate Passive Components]]




