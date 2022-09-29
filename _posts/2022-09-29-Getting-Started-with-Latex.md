---
title: Getting Started With Latex in 5 Minutes
permalink: getting-started-with-latex
date: 2022-09-29
excerpt: 
type: Blog
categories:
- Research
tags:
- latex
status: 
---

I started my Ph.D. last year at Clarkson University. I need to learn a lot of tools to cope with my research project and publish research articles. Latex is a new addition to my skill set, I have recently learned  Latex to write my first paper during Ph.D. Actually,  I have written multiple [papers](https://scholar.google.com/citations?user=ebLUEXQAAAAJ&hl=en) before. MS word was my way to go on these papers. Frankly speaking, it is really tempting to use MS word for writing papers as it seems easy to get started. Pain starts when you have written down a few pages and want to format the figure, refer to the figures and cite the paper.  There is no easy of in MS word for these. Here comes the Latex to rescue. 

In `LaTex`, you only need to focus on the content, the Latex engine handles the formatting for you. Your main job is to focus on writing not on formatting. Also managing references is very easy in latex. Here are the basic things you need to know to get started with Latex

### Class
 Controls the overall appearance of the document. This is the first thing you need to set for your project.
- `\documentclass{article}`:  An example article class
- `\documentclass[12pt, letterpaper]{article}`: Class takes additional parameter like font size and paper 
- Extension `.cls`. 
- [Official Class List](https://www.ctan.org/topic/class)

### Package
 Add more functionalities to the document.
 - `\usepackage{graphicx}`: Package to import external graphics files
 -  Extension: `.sty` 

### Body
 body of the document is written between the `\begin{document}` and `\end{document}` tags.
```latex
\documentclass{article}
\begin{document}
First document. This is a simple example, with no 
extra parameters or packages included.
\end{document}
```

### Preamble:
Everything before the `\begin{document}` is called setup or preamble
- Class and packages used in the document
- `\title{My first LaTeX document}`: the document title
- `\author{Shuvangkar Das}`: 
- `\date{August 2022}`: 

```latex
\documentclass[12pt, letterpaper]{article}
\title{Article on Latex By Shuvangkar Das}
\author{Shuvangkar das}
\date{August 2022}
```

### A Basic Latex File
```latex
\documentclass[12pt, letterpaper]{article}
\title{My first LaTeX document}
\author{Hubert Farnsworth\thanks{Funded by the Overleaf team.}}
\date{August 2022}
\begin{document}
We have now added a title, author and date to our first \LaTeX{} document!
\end{document}
```

### Bold, italics and underlining
- `\textbf{bold text}`
- `\textit{Italic Text}`
- `\underline{Underline Text}`

### Add Figures
- Need two packages to handle images/figures efficiently
	- `\usepackage{graphicx}`: Package for using graphics
	- `\graphicspath{{./FiguresPath}}`: Latex  look for images in the mentioned folder
- `\includegraphics{myimage.jpg}`: load  `myimage.jpg `
- `\includegraphics[width=15cm]{myfigure.pdf}`: You can mention the figure absolute or relative dimension. More details in [[Latex Figure]]
- To add caption, label and reference with the figure, the `figure` environment is used
```latex
\begin{figure}[h]
    \centering
    \includegraphics[width=0.75\textwidth]{myfigure.png}
    \caption{Figure Example by shuvangkar Das}
    \label{fig:referenceLink}
\end{figure}
```

### List
- Unordered list: `itemize` environment is used
```latex
\begin{itemize}
  \item First list
  \item Second list
\end{itemize}
```
- Ordered List: `enumerate` environment is used
```latex
\begin{enumerate}
  \item First list
  \item Second list
\end{enumerate}
```

### Math Equation 
For writing math, you do not need to load any package. It is by default supported. you can write math equations in-line with text and individual equations in display mode. 
- Inline math
	- `$E=mc^2$` or `begin{math} E=mc^2 end{math}` or ` `\( E=mc^2` \)`: Three command produce the same results
- Display math mode
```latex
\begin{equation}
	E=mc^2
	\label{eq2}
\end{equation}
```
If you want to refer to the equation, use label-text. 

### Paragraph and New Line
- `enter` key twice create paragraph or use `\\` 

---

-Shuvangkar Das, Potsdam, New York
### Interesting Things I am Doing Currently
Everyone does some form of knowledge work but most of the time does that inefficiently. As a result, despite working hard, we ended up with questionable results. So to address that I am working on a very exciting project name Smart Personal Knowledge Management(SPKM). In fact, I am making a YouTube video series on it. You can get update about the course in two ways, (1) by subscribing to my [YouTube](https://www.youtube.com/ShuvangkarDas) channel or (2) by subscribing my [newsletter](http://newsletter.shuvangkardas.com/)
### Connect with me
- Twitter: [https://twitter.com/shuvangkar_das](https://twitter.com/shuvangkar_das)
- LinkedIn: [https://www.linkedin.com/in/ShuvangkarDas/](https://www.linkedin.com/in/ShuvangkarDas/)
- YouTube: [https://www.youtube.com/ShuvangkarDas](https://www.youtube.com/ShuvangkarDas)
### References
1. https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes

