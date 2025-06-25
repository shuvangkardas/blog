---
title: Why Park Transformation (abc-dq) Confuses Everyone--A Practical Guide for Inverter Control
permalink: dq-transformation-confusion-park-transformation-inverter-control
date: 2025-06-25
excerpt: Understanding Park transformation is crucial for inverter control design in EMT simulations and firmware. This post breaks down the variants, their implications, and clears the confusion with real examples.
type: Blog
categories: 
tags: 
status:
---
When you are designing inverter control in EMT simulation or developing firmware for hardware, it is very important to understand Park transformation. Because, I call this the foundation block of control. Based on type of park transformation, you rest of control equations will be varied. For example think about cascaded current loop of inverter. It consists of 3 components, such as PI path for controlling the d-axis current, decoupling path $\omega L q$   and feedforward path $Vd$. Sign of these three components when summing mostly depends on the orientation of dq transformation. Same this goes for real and reactive calculation block.  

It has occurred to me many times that I used one convention of dq transformation and other convention of current controller design (with respect to sign). That was really a frustrating experience, I would say. Other time, I use power invariant type of transformation which preserves power in transformation but used power invariant version of the power equation from dq signals. Honestly speaking, the number of dq transformation types are confusing. 

Park transformation converts three-phase (abc) signals into a rotating dq reference frame. But the implementation varies based on:

1. **d-axis alignment** (usually with phase-a voltage or current)
2. **q-axis phase** (leading or lagging)
3. **Rotation direction** (clockwise or anti-clockwise)
4. **Power conservation** (Power Invariant vs Power Variant)


By combining these, you end up with many possible transformations—and hence, the confusion.

My goal here is to narrow down the the types so that I can discuss only with fewer variants. 

## Park Transformation Based on Power Conservation

1. Power Invariant 
2. Power Variant 
### 1. Power Invariant Transformation 
- Key property: power is conserved in $abc$ and $dq0$ frame
- P₃φ = P_dq0
- Scaling Factor: √(2/3) ≈ 0.816
- Magnitude Relationship: d-q components have magnitude = A × √(2/3) ≈ 0.816A. Here A is peak value


$$ \begin{align} \begin{bmatrix} d \\ q \\ 0 \end{bmatrix} &= \sqrt{\frac{2}{3}} \begin{bmatrix} \cos(0) & \cos(\theta-120°) & \cos(\theta+120°) \\ \sin(0) & \sin(\theta-120°) & \sin(\theta+120°) \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{bmatrix} \begin{bmatrix} a \\ b \\ c \end{bmatrix} \end{align} $$


### 2. Power Variant Transformation
- Key property: Peak values in abc frame = Peak values in d-q frame
- P_abc ≠ P_dq0 (power is scaled) 
- P_dq0 = (3/2) × P_abc

$$\begin{align} \begin{bmatrix} d \\ q \end{bmatrix} &= \frac{2}{3} \begin{bmatrix} \cos(\theta) & \cos(\theta-120°) & \cos(\theta+120°) \\ \sin(\theta) & \sin(\theta-120°) & \sin(\theta+120°) \end{bmatrix} \begin{bmatrix} a \\ b \\ c \end{bmatrix} \end{align}$$

## Narrow down transformation
In most control implementations I’ve worked with, I found the following combination to be the most effective:
- **Rotation**: Anti-clockwise
- **Type**: Power Variant
- **d-axis**: Aligned with phase-a voltage at t=0
    
Let’s now explore two variants in detail and validate their results with real calculations.


## Two Major Park Transformations 
### ✅ Variant 1: d-axis Aligned with Phase-a Axis
- **d-axis position**: Aligned with phase A axis (0°)
- **q-axis position**: 90° ahead of d-axis (counterclockwise) 
- $Us = U_d + jU_q$. This also says that $U_q$ is leading d by 90 degree


$$
\begin{aligned}
& U_s=u_d+j \cdot u_q \\
&=\left(u_a+j \cdot u_\beta\right) \cdot e^{-j \omega t} \\
&=\frac{2}{3} \cdot\left(u_a+u_b \cdot e^{\frac{-j 2 \pi}{3}}+u_c \cdot e^{\frac{j 2 \pi}{3}}\right) \cdot e^{-j \omega t} \\


\end{aligned}$$



Final Transformation
$$
\begin{aligned}
& {\left[\begin{array}{l}
u_d \\
u_q \\
u_0
\end{array}\right]=\frac{2}{3}\left[\begin{array}{ccc}
\cos (\omega t) & \cos \left(\omega t-\frac{2 \pi}{3}\right) & \cos \left(\omega t+\frac{2 \pi}{3}\right) \\
-\sin (\omega t) & -\sin \left(\omega t-\frac{2 \pi}{3}\right) & -\sin \left(\omega t+\frac{2 \pi}{3}\right) \\
\frac{1}{2} & \frac{1}{2} & \frac{1}{2}
\end{array}\right]\left[\begin{array}{l}
u_a \\
u_b \\
u_c
\end{array}\right]}
\end{aligned}
$$

#### Sample Calculation For Mag = 1, theta = 0 
The three-phase voltages are given by:

$$u_a = V_a = \sin(\omega t)$$
$$u_b = V_b = \sin\left(\omega t - \frac{2\pi}{3}\right)$$
$$u_c = V_c = \sin\left(\omega t + \frac{2\pi}{3}\right)$$
At $\omega t = 0$:
- $u_a = V_a = 0$
- $u_b = V_b = -0.866025$
- $u_c = V_c = 0.866025$

Since ωt = 0 values of matrix entries
- $\cos(0) = 1, \quad \cos(\pm 2\pi/3) = -\frac{1}{2}$
- $\sin(0) = 0, \quad \sin(-2\pi/3) = -\frac{\sqrt{3}}{2}, \quad \sin(2\pi/3) = +\frac{\sqrt{3}}{2}$

Row calculations:
- First row: $1 \cdot 0 + (-\frac{1}{2})(-0.866025) + (-\frac{1}{2})(+0.866025) = 0$
- Second row: $\frac{\sqrt{3}}{2} \cdot (-0.866025) + (-\frac{\sqrt{3}}{2}) \cdot (+0.866025) = -\frac{3}{2}$
- Third row: $\frac{1}{2} \cdot 0 + \frac{1}{2} \cdot (-0.866025) + \frac{1}{2} \cdot (+0.866025) = 0$

Scale by $\frac{2}{3}$:
$$\begin{align} \begin{bmatrix} u_d \ u_q \ u_0 \end{bmatrix} &= \frac{2}{3} M\mathbf{u} \ &= \frac{2}{3} \begin{bmatrix} 0 \ -\frac{3}{2} \ 0 \end{bmatrix} \ &= \begin{bmatrix} 0 \ -1 \ 0 \end{bmatrix} \end{align}$$

**Final result:** $u_d = 0, \quad u_q = -1, \quad u_0 = 0$


### ✅ Variant 2: Rotating frame 90 degree behind a-axis
- q-axis aligns with phase a-axis
- For a Mag = 1, phase  = 0 degree Then d = 1, q = 0
- d-axis is lagging phase-a axis by 90 degree
- Multiplying $Us = U_d + jU_q$  by $-j$ transform the equation into $U = -jU_d + U_q$



$$
\begin{align}
V_d &= \frac{2}{3}(V_a \sin(\omega t) + V_b \sin(\omega t - 2\pi/3) + V_c \sin(\omega t + 2\pi/3)) \\
V_q &= \frac{2}{3}(V_a \cos(\omega t) + V_b \cos(\omega t - 2\pi/3) + V_c \cos(\omega t + 2\pi/3)) \\
V_0 &= \frac{1}{3}(V_a + V_b + V_c)
\end{align}
$$

#### Sample Calculation For Mag = 1, theta = 0 
1. At $\omega t = 0$:
	- $u_a = V_a = 0$
	- $u_b = V_b = -0.866025$
	- $u_c = V_c = 0.866025$

2. Evaluate the sinusoidal multipliers at $ωt = 0$
	- $\displaystyle \sin(0) = 0$
	- $\displaystyle \sin\!\Bigl(-\tfrac{2\pi}{3}\Bigr) = -\frac{\sqrt{3}}{2}$
	- $\displaystyle \sin\!\Bigl(\tfrac{2\pi}{3}\Bigr) = +\frac{\sqrt{3}}{2}$
	- $\displaystyle \cos(0) = 1$
	- $\displaystyle \cos\!\Bigl(-\tfrac{2\pi}{3}\Bigr) = \cos\!\Bigl(\tfrac{2\pi}{3}\Bigr) = -\tfrac{1}{2}$
3. Substitute into the formulas and compute $V_d, V_q, V_0$
	- Compute $V_d$:
  
    $$\begin{aligned}
   V_d 
   &= \frac{2}{3}\bigl(V_a \sin 0 + V_b \sin(-\tfrac{2\pi}{3}) + V_c \sin(\tfrac{2\pi}{3})\bigr) \\
   &= \frac{2}{3}\Bigl(0 
       + \bigl(-\tfrac{\sqrt{3}}{2}\bigr)\bigl(-\tfrac{\sqrt{3}}{2}\bigr) 
       + \bigl(+\tfrac{\sqrt{3}}{2}\bigr)\bigl(+\tfrac{\sqrt{3}}{2}\bigr)\Bigr) \\
   &= \frac{2}{3}\Bigl(0 + \tfrac{3}{4} + \tfrac{3}{4}\Bigr)
   = \frac{2}{3} \cdot \frac{3}{2}
   = 1.
   \end{aligned}$$

	- Compute $V_q$

$$\begin{aligned}
   V_q
   &= \frac{2}{3}\bigl(V_a \cos 0 + V_b \cos(-\tfrac{2\pi}{3}) + V_c \cos(\tfrac{2\pi}{3})\bigr) \\
   &= \frac{2}{3}\Bigl(0 \cdot 1 
       + \bigl(-\tfrac{\sqrt{3}}{2}\bigr)\bigl(-\tfrac{1}{2}\bigr)
       + \bigl(+\tfrac{\sqrt{3}}{2}\bigr)\bigl(-\tfrac{1}{2}\bigr)\Bigr) \\
   &= \frac{2}{3}\Bigl(0 + \tfrac{\sqrt{3}}{4} - \tfrac{\sqrt{3}}{4}\Bigr)
   = \frac{2}{3} \cdot 0
   = 0.
   \end{aligned}$$

	- Compute $V_0$

   $$\begin{aligned}
   V_0 
   &= \frac{1}{3}(V_a + V_b + V_c) \\
   &= \frac{1}{3}\Bigl(0 + \bigl(-\tfrac{\sqrt{3}}{2}\bigr) + \bigl(+\tfrac{\sqrt{3}}{2}\bigr)\Bigr)
   = \frac{1}{3} \cdot 0
   = 0.
   \end{aligned}$$

**Final concise result:**
$$V_d = 1,\quad V_q = 0,\quad V_0 = 0 \quad\text{at }\omega t = 0\text{ for magnitude }1.$$

## ✅ Summary and Takeaway

The choice of Park transformation in inverter control is not trivial. Small mismatches in assumptions—such as whether the d-axis aligns with phase-a, or whether you're using power-invariant or variant forms—can significantly affect your control logic and stability.

### Key Recommendations:
- **Use power-variant transformation** for hardware-level inverter control.
- **Ensure consistency** in d-q frame orientation and controller design.
- **Validate with sample signals** before plugging into real firmware.

---

### Final Thoughts

I’ve made enough mistakes with inconsistent dq transformations to realize how critical it is to standardize your convention. Whether you're debugging an unstable controller in PSCAD or writing low-level code for F28335, getting this right is half the battle.

If you’re designing inverter controls or doing EMT simulations, I hope this post saves you hours of frustration and gives you a reliable mental model of Park transformation.

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
1. https://www.mathworks.com/help/sps/powersys/ref/abctodq0dq0toabc.html
2. [[Park Transformation Fundamentals]]



