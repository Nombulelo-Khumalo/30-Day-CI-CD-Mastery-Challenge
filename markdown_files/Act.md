# TEST PIPELINES LOCALLY, ACT ON WINDOWS

 **how `act` is used for local GitHub Actions testing**, **why it's needed**, and **how to set it up on Windows**.

---

## ✅ GitHub Actions Local Testing with `act`

### 📌 Why Use `act`?

[`act`](https://github.com/nektos/act) is a command-line tool that allows you to **run your GitHub Actions workflows locally**. This is useful for:

* Testing workflows **before pushing to GitHub**
* Saving time by avoiding repeated commits just to fix YAML issues
* Debugging CI/CD steps like linters, tests, builds, etc.

Instead of waiting for GitHub Actions to run in the cloud, `act` executes the same workflows **locally inside Docker containers**.

---

### ⚙️ How It Works

* `act` reads your `.github/workflows/*.yml` files
* It runs the steps inside Docker containers, simulating GitHub’s runner environment (e.g., `ubuntu-latest`)
* It supports different event types like `push`, `pull_request`, `workflow_dispatch`, etc.

---

### 💻 How to Install `act` on Windows

#### 1. **Download the binary**

* Go to: [https://github.com/nektos/act/releases](https://github.com/nektos/act/releases)
* Download: `act_Windows_x86_64.zip`
* Direct link: [Latest release download](https://github.com/nektos/act/releases/latest/download/act_Windows_x86_64.zip)

#### 2. **Extract and move it**

* Unzip it
* Move `act.exe` to a known location like:

```bash
C:\Tools\act\
```

#### 3. **Add `act` to your system PATH**

* Open "Edit system environment variables"
* Add `C:\Tools\act\` to the `Path` variable

#### 4. **Verify installation**

Open a new PowerShell or Command Prompt window:

```bash
act --version
```

You should see:

```bash
act version 0.2.80
```

---

### 🧪 How to Use `act` to Run GitHub Actions Locally

From the root of your project (where `.github/workflows/` lives):

```bash
act
```

To simulate a specific event:

```bash
act push
act pull_request
```

To see detailed logs:

```bash
act -v
```

---

### 🔧 Optional: Using a Custom Image

GitHub Actions use specific Docker images for runners. `act` can use a small default image, but for full compatibility you can use:

```bash
act -P ubuntu-latest=catthehacker/ubuntu:act-latest
```

---

### 📂 Example: Running a CI Workflow Locally

```bash
act push
```

This will run the same workflow that GitHub runs when you push to `main`.

---

### 🧩 Troubleshooting possible errors

* **Error about `act.exe not a valid app`** → Download the correct Windows version, not Linux or ARM.
* **Step fails locally but works on GitHub** → Ensure Docker is running and the container has access to the needed resources.

---

work smarter
