---
title: Getting Started with Scapy, A Practical Guide for Beginners
permalink: Scapy-cheatsheet
date: 2025-06-21
excerpt: Learn how to use Scapy from scratch to craft, sniff, and analyze network packets with Python. Whether you're diving into cybersecurity, building packet-based tools, or automating network testing, this guide walks you through real examples, protocol layers, packet editing, and PCAP handling—all with practical explanations. Start mastering the network stack with Scapy today.
type: Blog
categories: 
tags: 
status:
---


During my early exploration of network analysis and penetration testing, I stumbled upon Scapy. At first glance, it seemed like just another Python module. But once I got deeper, I realized its potential to manipulate packets exactly how I want—something that tools like Wireshark or tcpdump don't offer out-of-the-box. This blog post is intended for anyone who wants to get started with Scapy from scratch.

## What is Scapy?

Scapy is a powerful Python-based interactive packet manipulation tool. It allows you to create, modify, send, and sniff packets at various layers of the network stack. It supports numerous protocols and provides flexibility to work at both Layer 2 and Layer 3 of the OSI model.

## Installation

If you're using Kali Linux, chances are Scapy and Python 3 are already installed. But if not, you can install it via pip:

```bash
pip install scapy
```

Make sure to use `python3` when running Scapy scripts, especially if you encounter import errors.

## OSI Model Refresher

Before diving into Scapy, it helps to revisit the OSI model:

|Layer|Name|Data Unit|Function|
|---|---|---|---|
|7|Application|Data|Network process to application|
|6|Presentation|Data|Data representation & encryption|
|5|Session|Data|Interhost communication|
|4|Transport|Segments|End-to-end connections and reliability|
|3|Network|Packets|IP addressing and routing|
|2|Data Link|Frames|MAC addressing|
|1|Physical|Bits|Binary transmission|

In Scapy, the most commonly used layers are Data Link (Ethernet), Network (IP), and Transport (TCP/UDP).

## Scapy Packet Structure

Scapy constructs packets by stacking protocol layers. Here's a visual representation:

```
Ethernet / IP / TCP / Data
```

This means you can create a full packet from Layer 2 to Layer 7 using this simple syntax:

```python
from scapy.all import *
pkt = Ether()/IP(dst="1.1.1.1")/TCP(dport=80)/"GET / HTTP/1.1\r\n\r\n"
```

## Building Packets

You can build packets in multiple ways:

### Method 1: Inline

```python
pkt = Ether()/IP(dst='localhost')/TCP(dport=53, flags='S')
```

### Method 2: Modular

```python
l2 = Ether()
l3 = IP(dst='localhost')
l4 = TCP(dport=53, flags='S')
pkt = l2/l3/l4
```

Access any layer using:

```python
pkt[TCP]  # or pkt.getlayer(TCP)
```

## Viewing Packet Information

Here are essential commands to dissect packets:

|Command|Effect|
|---|---|
|`str(pkt)`|Assembles the packet|
|`hexdump(pkt)`|Hexadecimal dump of the packet|
|`ls(pkt)`|Lists all the fields|
|`pkt.summary()`|One-line summary|
|`pkt.show()`|Detailed view|
|`pkt.show2()`|Recalculates checksum before showing|
|`pkt.sprintf()`|Formatted string with field values|
|`pkt.decode_payload_as()`|Decodes payload differently|
|`pkt.psdump()`|Generates PostScript diagram|
|`pkt.pdfdump()`|Generates PDF with packet dissection|
|`pkt.command()`|Returns the Scapy command to recreate the packet|

## Sending and Sniffing Packets

### Sending Packets

```python
send(IP(dst="1.1.1.1")/ICMP())       # Layer 3
sendp(Ether()/IP(dst="1.1.1.1"))     # Layer 2
```

### Receiving Packets

```python
resp = sr1(IP(dst="1.1.1.1")/ICMP())
```

### Sniffing Packets

```python
def pkt_callback(pkt):
    pkt.show()

sniff(iface="eth0", filter="tcp", prn=pkt_callback, store=0)
```

Capture 3 packets:

```python
pkts = sniff(iface="eth0", count=3)
```

## Interface Management

### List Interfaces

```python
get_if_list()
```

### Get IP Address of Interface

```python
get_if_addr("eth0")
```

### On Windows

```python
from scapy.arch.windows import *
get_windows_if_list()
```

## Modifying Packets

Sometimes, you need to change values after a packet is constructed:

```python
pkt[TCP].sport = 4770
# Delete checksum and length fields to force recalculation
del pkt[TCP].chksum
del pkt[IP].chksum
del pkt[IP].len
pkt.show2()
```

## Reading/Writing PCAP Files

### Read

```python
pkts = rdpcap("sample.pcap")
```

### Stream Read

```python
from scapy.utils import PcapReader
reader = PcapReader("sample.pcap")
for pkt in reader:
    pkt.show()
```

### Write

```python
wrpcap("output.pcap", [pkt])
```

## Internal Representation

Scapy uses 3 representations for data:

|Type|Meaning|
|---|---|
|i|Internal (Python object)|
|m|Machine (Raw bytes)|
|h|Human-readable|

Example:

```python
m1 = MACField("mf", None)
i = m1.m2i(pkt, b'\x10\x02\x10\x02\x10\x02')
mbyte = m1.i2m(pkt, i)
print(i)       # "10:02:10:02:10:02"
print(mbyte)   # b'\x10\x02\x10\x02\x10\x02'
```

## Final Thoughts

Scapy is one of those rare tools that give you complete control over the networking stack, without requiring you to write low-level C code or deal with kernel modules. It becomes even more powerful once you start integrating it into automation scripts or pen-testing pipelines.

If you're just getting started, take your time to learn the building blocks. Play around with crafting and dissecting packets. With practice, you'll realize Scapy isn't just a tool—it's a networking playground for professionals.


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




