# 📅 Day 02 – Lint & Test Pipeline

## ✅ What did I build?

- A pipeline that runs linting with `flake8` and unit tests with `pytest` on every push or PR to `main`.

## 🔧 Tech Stack

- Python, Flask, Pytest, Flake8
- GitHub Actions

## 💥 Challenges

- Understanding runner environments
- Making sure dependencies are installed before running jobs

## 💡 Improvements

- Add test coverage report upload (tomorrow)
- Send notification on failed jobs

---

## 🎯 Interview Reflection

### ❓ Q1: Why use linting in CI?

**A:** Linting helps enforce code style and catch potential bugs before they reach production. Automating it ensures consistent quality.

### ❓ Q2: What is the difference between `flake8` and `pytest`?

**A:** `flake8` checks code style and syntax, while `pytest` runs unit tests to validate functionality.

### ❓ Q3: What happens if one step fails in GitHub Actions?

**A:** The job stops, and the pipeline is marked as failed unless the step has `continue-on-error: true`.

---

## 🧪 Bonus Practice Questions

1. How would you run only tests inside a specific folder using `pytest`?
2. How do you fail a pipeline if linting finds even one warning?
3. What is `set -e` and why is it useful in shell-based CI pipelines?
4. Why is caching Python dependencies useful in CI?

---
