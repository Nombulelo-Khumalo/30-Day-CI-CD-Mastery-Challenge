# 📅 Day 3 Dockerizing a Flask App

---

## 🎯 Interview Questions & Answers

### 1. What is Docker and why is it useful in CI/CD pipelines?

**Answer:**  
Docker is a containerization platform that allows you to package applications and their dependencies into isolated environments. It ensures consistency across development, testing, and production. In CI/CD, Docker helps build repeatable, environment-agnostic pipelines that reduce “it works on my machine” issues.

---

### 2. How do you create a Docker image from a Python application?

**Answer:**  
You create a `Dockerfile` with instructions to:

- Set a base image (e.g. `python:3.10-slim`)
- Copy source code into the image
- Install dependencies using `pip`
- Define the command to run the app (e.g. `CMD ["python", "main.py"]`)  
Then run `docker build -t image_name .`

---

### 3. What does `.dockerignore` do?

**Answer:**  
`.dockerignore` excludes files and directories from being copied into the Docker image. It works like `.gitignore` and helps reduce image size and build time by excluding unnecessary files like `.git`, `__pycache__`, etc.

---

### 4. How do you run a Docker image in GitHub Actions?

**Answer:**  
In your GitHub Actions workflow:

```yaml
- name: Build Docker image
  run: docker build -t myapp .

- name: Run Docker container
  run: docker run myapp
```

You need to ensure that the runner environment supports Docker (e.g. `ubuntu-latest`).

---

### 5. Why might you containerize a Python microservice?

**Answer:**
To ensure consistent environments, facilitate deployment across different systems, isolate dependencies, enable scaling with orchestration tools like Kubernetes, and improve CI/CD automation.

---

## 🎁 Bonus Questions

1. What’s the difference between a container and a virtual machine?
2. How can you optimize Docker images for speed and size?
3. How would you run tests inside a Docker container?
4. Can you explain multi-stage builds in Docker?
5. What are best practices for writing Dockerfiles?
6. How would you deploy a Dockerized app to production?
7. What Docker command lists all running containers?
8. How do you stop and remove all containers using a single command?

---
