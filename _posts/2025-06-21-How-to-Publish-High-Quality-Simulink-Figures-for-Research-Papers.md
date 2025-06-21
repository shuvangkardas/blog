---
title: How to Publish High-Quality Simulink Figures for Research Papers
permalink: how-to-publish-high-quality-simulink-figures
date: 2025-06-21
excerpt: 
type: Blog
categories: 
tags: 
status:
---
If you're working on a thesis, research paper, or technical documentation, you’ve likely struggled with making your Simulink plots publication-ready. I’ve been there—figures that looked fine on-screen turned blurry or misaligned when exported. In this tutorial, I’ll walk you through the exact process I follow to edit and export Simulink figures from `.fig` format into clean, high-resolution images suitable for professional publishing. Whether you're a student or a researcher, this guide will save you hours of formatting and help your figures look polished and precise.


## Why Use `.fig` Format?
Simulink allows you to save figures in MATLAB’s native `.fig` format, which stores all properties of the plot—axis labels, legends, line widths, colors, font sizes. This makes it much easier to update your figure without rerunning the entire simulation.


## Step-by-Step Plot Editing Workflow

### Step 1: Save Your Simulink Plot as `.fig`

After running your Simulink model, go to the plot window and - Save the Figure in `.fig` format 

This preserves the full object structure and makes the figure editable later.

### Step 2: Open and Edit the `.fig` File

Open the `.fig` file using MATLAB. Navigate to:

`Tools` → `Edit Plot`

Now double-click on any plot element (axis, line, label). A property editor window will pop up.

### Step 3: Update Axis Colors and Properties
You can now:
- Change X and Y axis label color and font
- Adjust axis limits
- Add gridlines
- Customize tick marks

![Image](/assets/images/Pasted-image-20250621082833.png)
<sub>_Change fig axis color_</sub>  


### Step 4: Change Line Width and Color
To enhance visibility, double-click on any line or signal and update its line width and color from the pop-up.

![Image](/assets/images/Pasted-image-20250621082823.png)
<sub>_Changing line thickness for clarity:_</sub>  


![Image](/assets/images/Pasted-image-20250621083731.png)
<sub>_Example of axis property editor:_</sub>  

## Exporting the Figure for Publication
Once your figure is finalized, use the following script to export it in high resolution (300 DPI) and a specific image size.

```matlab
clear all; close all; clc;

fidName = 'Xfmr_LV_PhaseC_Current_Harmonics';
imageName = "2.3_Xfmr_LV_PhaseC_Current_Harmonics.png";

% Open the .fig file
fname = strcat(fidName,'.fig');
p1 = openfig(fname);

% Update Line Width
hline = findobj(gcf, 'type', 'line');
set(hline,'LineWidth',1.2)

% Set axis font size and grid
grid on;
set(gca,"FontSize",11);

% Set image size and resolution
imageWidth = 4.5;
imageHeight = 3;
imageDPI = '-r300';
imageFormat = '-dpng';

set(gcf,"Units","inches");
set(gcf,"position",[0,0,imageWidth,imageHeight])
print(imageName,imageFormat, imageDPI);

```

## Final Tips for High-Quality Figures
- Use consistent font sizes and line widths across all your figures.
- Always preview the final PNG or PDF before inserting into your paper.
- Stick to grayscale or color-blind-friendly palettes if publishing in print journals.
- Maintain 300 DPI or higher for professional publication.

---
## 🛠️ Quick Recap
- ✅ Save your Simulink figure as `.fig`
- ✅ Use `Edit Plot` to customize elements
- ✅ Adjust line widths and font sizes manually
- ✅ Export using a script with proper DPI and image size



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
[[Simulink Fig File Print Methods]]



