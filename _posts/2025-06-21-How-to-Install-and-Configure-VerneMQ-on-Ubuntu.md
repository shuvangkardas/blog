---
title: How to Install and Configure VerneMQ on Ubuntu (Beginner-Friendly Guide)
permalink: vernemq-ubuntu-setup-guide
date: 2025-06-21
excerpt: Setting up VerneMQ on Ubuntu doesn’t have to be difficult. In this beginner-friendly guide, I’ll walk you through the easiest way to install, configure, and run VerneMQ without the hassle of building from source. Whether you're testing MQTT clients or exploring message brokers, this quickstart guide has you covered.
type: Blog
categories: 
tags: 
status:
---
If you're just starting with MQTT and looking for a scalable message broker, **VerneMQ** is a great choice. It’s high-performance, MQTT-compliant, and supports clustering. But getting it up and running — especially from source — can be a challenge.

In this guide, I’ll show you how I got VerneMQ running on Ubuntu **without dealing with Erlang builds** or dependency issues. Perfect for testing and development.

---
## Why I Chose Binary Installation
VerneMQ offers two ways to install:

1. From source (requires Erlang and its dependencies)
2. From binary packages

I tried both — and honestly, building from source was time-consuming and dependency-heavy. If you're looking for a quick and reliable setup, **use the binary package**.

---

## ✅ Step 1: Download and Install VerneMQ

Head over to the official [VerneMQ downloads page](https://vernemq.com/downloads/) and get the `.deb` package.

```bash
# Install the downloaded package
sudo dpkg -i <package_name>
```

---

## ✅ Step 2: Accept the License (EULA)

After installing, you need to accept the End User License Agreement (EULA) before starting VerneMQ.

Edit the config file:

```bash
sudo nano /etc/vernemq/vernemq.conf
```

Uncomment or add:

```bash
accept_eula = yes
```

Save and close the file.

---

## ✅ Step 3: Start and Test VerneMQ

Start or restart the service:

```bash
sudo systemctl restart vernemq
```

Check if it’s running:

```bash
sudo vernemq ping
```

---

## ✅ Step 4: View and Configure Listeners

By default, VerneMQ listens on `127.0.0.1:1883`. To connect external MQTT clients, you’ll need to expose a new listener:

### View current listeners:

```bash
sudo vmq-admin listener show
```

### Start a new listener:

```bash
sudo vmq-admin listener start address=192.168.0.110 port=1884 --mountpoint /test --nr_of_acceptors=10 --max_connections=1000
```

Then confirm:

```bash
sudo vmq-admin listener show
```

> 🛑 **Note**: Replace `192.168.0.110` with your machine’s IP address.

---

## ✅ Step 5: (Optional) Disable Authentication for Testing

To quickly test your MQTT clients, you can disable authentication:

```bash
# In /etc/vernemq/vernemq.conf
allow_anonymous = on
```

> ⚠️ **Warning**: This is **not safe for production**. Only use it in local testing environments.

---

## ✅ Step 6: Configure Listening Ports (Alternate Method)

You can also define multiple listeners directly in the config file:

```bash
# Inside /etc/vernemq/vernemq.conf
listener.tcp.default = 127.0.0.1:1883
listener.tcp.local = 192.168.0.110:1884
```

Now, VerneMQ will listen on both ports — one for localhost and one for your local network.

---

## ✅ Step 7: Check Port Availability (Telnet)

To ensure the MQTT port is open:

```bash
telnet 192.168.0.110 1884
```

If the port is open, the screen will clear. Otherwise, you'll see a connection error.

---

## ✅ Step 8: Disable Firewall (for Testing Only)

If you're having trouble connecting:

```bash
sudo ufw disable     # for testing
sudo ufw enable      # re-enable after testing
```

> ⚠️ Again, **don’t disable firewalls permanently** in a production system.

---

## ✅ Step 9: Access the Local Dashboard

If you’ve installed the dashboard plugin, it might be accessible at:

```
http://localhost:8888/status
```

Not all installations include the dashboard, but it’s a helpful tool if configured.

---

## Final Thoughts

This guide is meant for **testing and exploration**. VerneMQ has powerful features like clustering, plugins, and authentication integrations that you can explore further once you're comfortable with the basics.

If you just want to see MQTT messages flowing from a client to a broker — this setup will get you there.

---

## What’s Next?

Once VerneMQ is up and running:
- Try connecting with **MQTT.fx**, **MQTT Explorer**, or Python's `paho-mqtt`
- Explore **user authentication and ACLs**
- Set up **clustering** for high availability


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




