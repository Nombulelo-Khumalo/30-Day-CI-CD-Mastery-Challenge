# 📅 Day 01 – Hello Pipeline

## ✅ What did I build?

I created my first CI/CD pipeline using GitHub Actions that triggers on every push to `main`. It prints a hello message, shows the system date, and runs a basic shell script to verify the CI runner is working.

---

## 🔧 Technologies Used

- GitHub
- GitHub Actions
- Bash scripting

---

## 💥 Challenges Encountered

- Workflow not triggering until I learned it must be in `.github/workflows` at the repo root
- Minor YAML formatting details (spacing, indentation, filename conventions)

---

## 🎯 What I Would Improve

- Add more useful diagnostics (runner OS, env vars)
- Include job success/failure emoji notification

---

## 🧠 Interview Simulation

### ❓ Q1: What is CI/CD?

**A:** CI/CD stands for Continuous Integration and Continuous Deployment (or Delivery). It automates building, testing, and deploying code to increase speed and reliability of software releases.

---

### ❓ Q2: What does `runs-on: ubuntu-latest` mean?

**A:** It tells GitHub to execute the job on a fresh Ubuntu VM runner hosted by GitHub.

---

### ❓ Q3: What are `jobs` and `steps` in GitHub Actions?

**A:** A `job` is a set of tasks run on the same runner. A `step` is a single action or command inside that job. Steps run sequentially.

---

### ❓ Q4: Where must GitHub workflow files live?

**A:** Inside `.github/workflows/` at the **root** of the repo. Not in subfolders.

---

### ❓ Q5: What happens if a step fails in a GitHub Actions job?

**A:** The job fails and all following steps in that job are skipped, unless `continue-on-error` is set.

---

## 🧪 Bonus Questions

1. How can you manually trigger a workflow in GitHub Actions?
2. How do you debug a failed workflow run?
3. How would you change the pipeline to only run on pull requests?
4. What is the default shell used in GitHub Actions?
