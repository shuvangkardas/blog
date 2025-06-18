---
title: "Docker Cheatsheet: Everything You Need to Get Started"
permalink: docket-Cheatsheet
date: 2025-06-18
excerpt: 
type: Blog
categories: 
tags: 
status:
---

Whether you're a beginner or just need a quick reference, this Docker cheatsheet will help you install Docker, run containers, create your own images, and use Docker Compose with confidence.

---

## Installing Docker on Ubuntu

Start by removing any old versions:

```bash
sudo apt-get remove docker docker-engine docker.io containerd runc
```

The easiest way to install Docker is via their official convenience script:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

Check Docker version:

```bash
docker --version
```

📖 Full installation guide: [Official Docs](https://docs.docker.com/engine/install/ubuntu/)

---

## Basic Docker Commands

|Task|Command|
|---|---|
|Run a container|`docker run nginx`|
|List running containers|`docker ps`|
|List all containers|`docker ps -a`|
|Stop a container|`docker stop <container_name>`|
|Remove a container|`docker rm <container_name>`|
|List all images|`docker images`|
|Remove an image|`docker rmi <image_name>`|
|Pull an image|`docker pull nginx`|
|Run a command inside a container|`docker exec <container_id> <command>`|
|View container details|`docker inspect <container_id>`|

📝 **Note:** A container stops when the process inside it stops.

---

## 🖥️ Access Docker Container Shell

```bash
docker exec -it <container_name_or_id> bash
```

---

## Port Mapping

Expose a container’s internal port to the outside world:

```bash
docker run -p 80:5000 kodeloud/simple-webapp
```

Here, `80` is your host port, and `5000` is the container port.

---

## Folder Mapping (Volumes)

Map a host directory to a container directory to persist data:

```bash
docker run -v /host/dir:/container/dir mysql
```

---

## View Container Logs

```bash
docker logs <container_id>
```

---

## Run Containers in Background (Detached Mode)

```bash
docker run -d ubuntu sleep 100
```

To attach later:

```bash
docker attach <container_id>
```

---

## Creating Your Own Docker Image

1. Write a `Dockerfile`
    
2. Build the image:
    

```bash
docker build -t your_username/app_name .
```

3. Push to Docker Hub:
    

```bash
docker push your_username/app_name
```

### Dockerfile Basics

```Dockerfile
FROM ubuntu

RUN apt-get update && apt-get install -y python3 pip
RUN pip install flask flask-mysql

COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
```

📌 Key Points:

- `FROM` defines the base image.
    
- `RUN` executes commands.
    
- `COPY` brings files into the image.
    
- `ENTRYPOINT` defines the default command when the container starts.
    

---

## Try Docker Manually

```bash
docker run -it ubuntu bash
apt-get update
apt-get install -y python3 pip
```

---

## Install Docker Compose

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

---

## Dockerfile vs Docker Compose

- **Dockerfile**: Describes how to build a single image.
    
- **docker-compose.yml**: Describes how to run multi-container applications.
    

💡 **Workflow**:

1. Build images with Dockerfile.
    
2. Define containers with `docker-compose.yml`.
    
3. Run the stack using Docker Compose.
    

---

## Docker Compose Commands

|Task|Command|
|---|---|
|Launch in background|`docker-compose up -d`|
|Set custom image name|`docker-compose --project-name myapp up`|
|Validate config|`docker-compose config`|

---

## Clean Up Docker

```bash
# Stop all running containers
docker stop $(docker ps -aq)

# Remove all containers
docker rm $(docker ps -aq)

# Remove all images
docker rmi $(docker images -q)
```

---

## 🔗 Useful References
- [Docker Official Docs](https://docs.docker.com/)
- [Docker Compose Docs](https://docs.docker.com/compose/)
- [Docker Hub](https://hub.docker.com/)
    
---
## Final Tips

- Always name your containers and volumes for easier management.
- Use `.dockerignore` like `.gitignore` to avoid copying unnecessary files.
- Combine multiple `RUN` instructions into one to reduce image layers.
    

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




