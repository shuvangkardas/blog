---
title: How I Saved 5 Hours by Building My Own AI Transcriber Locally (You Can Do the Same)
permalink: how-to-transcribe-locally
date: 2025-06-26
excerpt: Tired of rewatching videos for one detail? See how I use AI to transcribe 1-hour videos in minutes—offline and for free.
type: Blog
categories: 
tags: 
status:
---
I recently had to write a report from a 1-hour-long seminar. I had slides and a recording—everything I needed. Still, the thought of playing it back, pausing, rewinding, and writing notes felt like a 5–6 hour chore.

But instead of grinding through it, I spent **just one hour**.  
💡 **30 minutes to build a transcription script**  
💡 **30 minutes to edit the report using the transcript**

This is where **local AI automation** shines—and if you're a researcher, engineer, or obsessive note-taker like me, this post might just change your workflow.

---

## Why I Built a Local Transcription Setup

I’ve always loved **automating repetitive tasks**. It’s not just about saving time—it’s about doing work _once_ and reusing it forever. As someone who takes notes extensively in **Obsidian**, I regularly capture content from YouTube videos, webinars, and Zoom lectures.

Why?

Because when I need to revisit a specific detail, I don't want to watch an entire video again. I want to **search my notes instantly**. That’s where transcription comes in.

---

## Why I Don’t Use Online Services
There are many transcription tools online, but most have one or more of the following issues:
- Limited to 30-minute videos
- Slow processing or queue times
- Paid subscriptions or hidden costs
- **Privacy risks**—especially critical when dealing with internal or corporate resources

Most companies don’t allow uploading internal meetings to third-party servers. **Local transcription is the only option.** I’ve even used this for missed seminars—transcribing them and extracting key ideas in minutes.

---

## How to Set Up Local Video Transcription with Whisper

Let’s walk through the process to set up **Whisper**, OpenAI’s powerful transcription model, locally on your machine.

### Step 1: Create a Python Environment
First, create and activate a Conda environment:

```bash
conda create --name transcribe python=3.10
conda activate transcribe
```

---

### Step 2: Install Required Packages

Install Whisper and necessary tools:
```bash
pip install openai-whisper
pip install torch torchvision torchaudio
conda install -c conda-forge ffmpeg
```

---

### Step 3: Verify Installation
Before using Whisper, make sure it's installed correctly:

```python
import whisper
import subprocess

try:
    subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
    print("FFmpeg accessible from Python")
except Exception as e:
    print(f"FFmpeg issue: {e}")

try:
    model = whisper.load_model("tiny")
    print("✅ Whisper model loaded successfully")
except Exception as e:
    print(f"Whisper issue: {e}")
```

Expected Output:
```
FFmpeg accessible from Python 
Whisper model loaded successfully
```

---

## 📝 Transcribe Your Video or Audio

Here’s the script I use to transcribe any video file and automatically save the output in a `.txt` file.

```python
import whisper
from pathlib import Path

VIDEO_PATH = r"..\Obsidian\01 Obsidian Getting Started\00 Obsidian Getting Started V2.mov"
MODEL_SIZE = "base"
LANGUAGE = None  # Set to "en", or leave None for auto-detect

def transcribe_video():
    model = whisper.load_model(MODEL_SIZE)
    print(f"Transcribing: {Path(VIDEO_PATH).name}")
    
    result = model.transcribe(VIDEO_PATH, language=LANGUAGE)
    
    output_path = Path(VIDEO_PATH).parent / f"{Path(VIDEO_PATH).stem}_transcription.txt"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result["text"])

    print(f"Saved to: {output_path}")
    print("\nPreview:\n", result["text"][:300], "...")
    return result["text"]

if __name__ == "__main__":
    transcribe_video()
```

---

## My Workflow: Whisper + Obsidian = Instant Knowledge

I save each transcription in Obsidian, link it with related notes, and build a searchable, permanent second brain. Now if someone asks what was discussed in a 90-minute session last year, I have the answer in seconds.

---

## Final Thoughts

This tiny setup has saved me **countless hours**—and it cost me **nothing**. No waiting. No cloud. Just **offline AI-powered transcription** on my own terms.

If you value your time, your data, and your productivity—build this once, and thank yourself every week.

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
[[Setup Local Transcription]]



