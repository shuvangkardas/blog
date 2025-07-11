---
title: How To Remember Confusion Matrix; True Positive, True Negative, False Positive And False Negative
permalink: understand-confusion-matrix
date: 2022-08-19
excerpt: 
type: Blog
categories: 
tags:
  - machine-learning
  - theory
status:
---

Every time I read about these four terms i.e. True Positive(TP), True Negative(TN), False Positive(FP), and False Negative, I thought that I got it. Later I get confused and then mess up. I guess this happens with you too. Maybe this is the reason these four terms are called confusion matrix or Error Matrix. 
![Image](/assets/images/Confusion-Matrix-Fun-Example.png)

After Googling these terms I came into this medium blog[^1] of Sarang Narkhede. The picture you see at the top, taken from there and it is convincing. Still, I am not sure about remembering these terms. 

{% include newsletter.html %}

For remembering things, I always believe in connection. Connection is the best way to store things for the long term. If you read the book How to Take Smart Notes by Sönke Ahrens, you will get a good example of remembering the difference between artery and vein by creating connection with old knowledge. That's my favorite example. Ok! lot of pep talk. Let's come to the point. 

The confusion matrix is a table of 4 different combinations of predicted and actual values[^1]. All these terms consist of two words. The first part consists of True/False and the second part Positive/Negative.
You need to remember **two connections** to understand the confusion matrix:
1. **Second part(Positive/Negative) is the predicted value. That comes from your model or test**
2. **First part(True/False) verifies the second part. Whether the second part(prediction) is true or false.**

Consider a hypothetical scenario. A pregnancy test was done on urine samples of a man and woman. The woman is pregnant. Also, look into the picture. 
- **True Positive:** The prediction is **Positive**(women pregnant) that is **True**
- **True Negative:** The prediction is **Negative**(man not pregnant) that is **True**

This time the nurse forgetfully swapped the urine sample of the pregnant woman with a man 😋.
- **False Positive:** The prediction is **Positive**(man pregnant) that is **False** and impossible!
- **False Negative:** The prediction is **Negative**(Women not pregnant) that is **False**


Now Read the two rules again. You will remember the confusion matrix for life. 

✅ _If you find this kind of relatable breakdown helpful, I share more simple explanations like this — real stories and practical lessons — straight to your inbox. No spam, just once a week._  
{% include newsletter.html %}


---
### 👋 About Me
Hi, I’m **Shuvangkar Das** — a power systems researcher with a Ph.D. in Electrical Engineering, currently working as a Research Engineer at EPRI. I work at the intersection of power electronics, inverter-based DERs (IBRs), and AI to help build smarter, greener, and more stable electric grids. 

My work spans large-scale EMT simulations, firmware development, reinforcement learning, and hardware prototyping. Beyond engineering, I’m also a [YouTuber](https://www.youtube.com/@ShuvangkarDas) and content creator — sharing hands-on insights on productivity, research, and knowledge management. My goal is simple: to make complex ideas more accessible and actionable for everyone.

**Real stories. Practical lessons. Right in your inbox.**  
No spam—just once a week.  
{% include newsletter.html %}

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

### 📚 References/Obsidian Notes
[^1]: https://towardsdatascience.com/understanding-confusion-matrix-a9ad42dcfd62
[[Confusion Matrix]]



---
Shuvangkar Das, Potsdam, New York

Connect with me:
- Twitter: [https://twitter.com/shuvangkar_das](https://twitter.com/shuvangkar_das)
- LinkedIn: [https://www.linkedin.com/in/ShuvangkarDas/](https://www.linkedin.com/in/ShuvangkarDas)
- YouTube: [https://www.youtube.com/ShuvangkarDas](https://www.youtube.com/ShuvangkarDas)

## References
[^1]: https://towardsdatascience.com/understanding-confusion-matrix-a9ad42dcfd62