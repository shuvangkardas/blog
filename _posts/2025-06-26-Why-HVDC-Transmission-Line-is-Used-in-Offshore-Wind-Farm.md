---
title: Why HVDC is Used in Offshore Wind Farms--A Lesson from My 9GW EMT Simulation Project
permalink: offshore-wind-hvdc-vs-hvac-transmission
date: 2025-06-26
excerpt: _Learn why HVDC is the preferred transmission method in offshore wind farms based on real-world experience from a 9GW EMT simulation project involving 8 offshore farms in New York. Understand the technical and economic reasons behind HVDC’s dominance over HVAC for long-distance submarine cables._
type: Blog
categories: 
tags: 
status:
---
During my PhD, I had the opportunity to work on one of the largest power system simulation projects in the state of New York—a **9 GW offshore wind farm integration study** using **EMT (Electromagnetic Transient) simulation**. This project was part of New York’s ambitious plan to achieve clean energy targets, and the complexity was unlike anything I had worked on before.

The scope was massive. We were simulating **eight offshore wind farms** in detail—**three HVAC**-based and **five HVDC**-based connections. Each one had to be modeled with accuracy, and the interactions with the onshore grid—especially around **New York City and Long Island zones**—had to be studied under different operating and fault conditions.

> “The offshore wind farms will account for nearly 25% of the total state’s power generation and mainly penetrate the New York City and Long Island zones,”  
> — _Thomas Ortmeyer, Director of Clarkson’s Center for Electric Power System Research_[^1]

---
![Image](/assets/images/Pasted-image-20250626064434.png)
### ⚡ The Question That Changed My Understanding

While working of the models and running EMT simulations, one question kept hitting me:

**Why were most of the offshore wind farms using HVDC for exporting power to shore, and not HVAC?**

It felt counterintuitive at first. After all, HVAC is more familiar and often cheaper in short-range transmission. So I started digging deeper. Here’s what I learned—summarized for anyone wondering the same.

---

### 🔌 HVAC vs HVDC: What's the Technical Deal?

#### 📉 AC (HVAC) Transmission Limitation Over Distance

One of the major drawbacks of HVAC cables—especially submarine ones—is **charging current**. The longer the cable, the more reactive power it produces, limiting how much _real power_ you can transmit.
- The **charging current** grows with distance and voltage, which means you can’t use the entire current-carrying capacity for actual power delivery.
- This means HVAC becomes inefficient and costly as distance increases.


![Image](/assets/images/Pasted-image-20250626064545.png)

As shown above, the transmission capacity of HVAC submarine cables **declines rapidly beyond 80–100 km**, even with higher voltage levels.[^2]

#### ⚙️ Why HVDC Works Better for Offshore Wind
- **No charging current**: HVDC doesn’t suffer from capacitive charging losses.
- **Lower transmission losses**: Especially over long distances, HVDC transmits power more efficiently
- **Higher power density**: More power can be transmitted per conductor.
- **Better voltage control**: Less affected by impedance and voltage drops, making it more stable for weak grid conditions.
- **Easier integration into grid codes**: Especially with VSC-HVDC, the converter can be tuned for specific grid behaviors.

---

### 💡 Summary: Why HVDC is the Go-To for Offshore Wind

When the offshore wind farm is **more than 80–100 km** away from shore, HVAC becomes uneconomical due to:

- High reactive power generation
- Power transmission limits
- Need for costly compensation equipment

On the other hand, **HVDC systems shine** for such cases by:
- Enabling **efficient long-distance power export**
- Reducing cable and system losses
- Supporting **large-scale renewable integration**

---

### 🧠 Final Thought

That one question during my PhD—_“Why HVDC?”_—led me down a path of understanding not just simulation, but **real-world engineering decisions** in power systems. I realized that every transmission design choice is a balance of **distance, capacity, stability, and economics**.

If you’re working on power system planning, especially in the era of renewables, understanding **HVDC vs HVAC** trade-offs is not optional—it’s fundamental.


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
[^2]: H. Pfeifenberger, J. Tsoukalis, and S. Newell, “The Benefit and Cost of Preserving the Option to Create a Meshed Offshore Grid for New York,” 2021.

 [[Why HVDC Transmission Line is Superior]]
