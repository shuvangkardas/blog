---
title: How to Get Unlimited Zotero Storage Using Google Drive and ZotFile – A Step-by-Step Guide for Researchers
permalink: zotero-unlimited-storage-google-drive-zotfile-setup-guide
date: 2025-06-24
excerpt: If you're tired of Zotero's 300MB storage limit, here's a free, simple method to sync unlimited PDFs using Google Drive and ZotFile. I've used this workflow for over a year while writing 8+ papers during my PhD. Here's exactly how I did it.
type: Blog
categories: 
tags: 
status:
---
At the end of 2022, I created a set of YouTube playlists on [Build Your Second Brain](https://www.youtube.com/playlist?list=PLTmvRP1LI8sUi3AIMPGl3AiSSnl43E7Nh), [Obsidian for Beginners](https://www.youtube.com/playlist?list=PLTmvRP1LI8sWc4vkaee2XSRkly-wBACQw) and [Zotero for Beginners](https://www.youtube.com/playlist?list=PLTmvRP1LI8sWc4vkaee2XSRkly-wBACQw). One video stood out — _How to get unlimited Zotero storage_. It resonated with thousands of viewers, especially PhD students and researchers like me who write a lot but don’t want to pay for Zotero’s limited free storage.


<iframe width="560" height="315" src="https://www.youtube.com/embed/MfFXQ5JYPeA?si=p-Z8UMxKp88fa4_k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Step 1: Understand How Zotero Stores Files
You need to remember two key points for managing Zotero storage:
1. **Storage of Attachments**: Zotero stores all PDFs, attachments, images, and similar files in uniquely identified folders. As you add more PDFs, Zotero creates additional folders to hold them. These attachments consume the majority of your Zotero storage. To save space, you can move these attachments to a cloud service like Google Drive or OneDrive.
    
2. **Storage of Metadata**: Zotero uses an SQLite database to store metadata such as titles, authors, tags, and links to attachments. Since this is a binary file, typical cloud services cannot sync it reliably. That’s why Zotero offers its own sync service, which includes 300MB of free storage—sufficient for syncing this metadata database.

💡 **Strategy**:  
Use Zotero’s built-in sync service for syncing your metadata (up to 300MB, which is typically enough), and use Google Drive (or similar) to store and sync your attachments. This setup gives you unlimited storage for your PDFs while keeping your Zotero library in sync.



### Step 2: Configure Zotero Sync Settings
Now to sync Zotero database, setup Zotero 300MB default sync service from `Zotero > Preferences > Sync`
![Image](/assets/images/Pasted-image-20250624063104.png)


### Step 3: Set Zotero and ZotFile Base Directory
#### Define Attachment Location in Zotero
- Create a folder in your Google Drive (e.g., `Zotero_Attachments`).
- Open Zotero → **Edit > Preferences** (or **Zotero > Preferences** on macOS).
- Go to the **Advanced** tab → under **Files and Folders**, click **Choose** next to _Linked Attachment Base Directory_.
- Select the Google Drive folder you created.
- Repeat this setup on other devices (the path may vary).
![Image](/assets/images/Pasted-image-20250624063144.png)

#### Set Same Folder in ZotFile
Now you Need Zotfile pluging to install. If you face problem with installing Zotfile, please watch my Zotero for Beginners video series. 
Now, Select the same Google drive location in ZotFile Preferences.
![Image](/assets/images/Pasted-image-20250624063154.png)


### Drawbacks of This Setup
- ✅ Works perfectly across multiple PCs and laptops.
- ❌ Does **not** work well with iPads or Zotero Mobile, as **linked files** are not supported.
- 🔄 Alternative? Consider **WebDAV** in future — it supports attachment syncing across platforms.


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
[[Zotero Syncing Using Google Drive]]



