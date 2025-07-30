# TECH STACK

## A clear tech stack ensures *focus*, *repeatability*, and *real-world alignment*

---

## 🧰 **CI/CD Core Tools**

| Tool               | Purpose                                      |
| ------------------ | -------------------------------------------- |
| **GitHub Actions** | Primary CI/CD engine (runs 70% of pipelines) |
| **Jenkins**        | Industry-standard for self-managed CI/CD     |
| **GitLab CI**      | Bonus for GitLab-hosted projects             |
| **CircleCI**       | Cloud-native CI/CD with strong caching       |
| **ArgoCD**         | GitOps controller for Kubernetes             |
| **Terraform**      | Infrastructure as Code for AWS resources     |
| **Helm**           | K8s package manager (advanced deploys)       |

---

## ☁️ **Cloud Providers & Platforms**

| Platform                                | Use                                                          |
| --------------------------------------- | ------------------------------------------------------------ |
| **AWS (main)**                          | EC2, S3, EKS, Lambda, Secrets Manager, CodeDeploy            |
| **DockerHub/GitHub Container Registry** | Image registry                                               |
| **GCP (light use)**                     | For multi-cloud challenge                                    |
| **GitHub**                              | Source of truth for all code, pipelines, and version control |

---

## ⚙️ **Languages + Runtimes**

| Language            | Used For                                                     |
| ------------------- | ------------------------------------------------------------ |
| **Python**          | App + test examples, linting, unit testing                   |
| **Node.js (JS/TS)** | Frontend builds (e.g., React/Next.js) + test examples        |
| **Bash**            | Scripting in workflows and EC2 deploys                       |
| **YAML**            | Defining all CI/CD workflows (Actions, GitLab, ArgoCD, etc.) |

---

## 📦 **Containerization & K8s**

| Tool                             | Use                                     |
| -------------------------------- | --------------------------------------- |
| **Docker**                       | All apps containerized for portability  |
| **Docker Compose**               | Multi-container local dev + build CI    |
| **Kubernetes (EKS or Minikube)** | Real-world deploys (week 3+)            |
| **kubectl**                      | CLI to manage K8s                       |
| **Helm**                         | Advanced deploys and templating for K8s |

---

## 🔐 **Security & Secrets**

| Tool                               | Use                                     |
| ---------------------------------- | --------------------------------------- |
| **GitHub Secrets**                 | CI secrets (tokens, keys)               |
| **Snyk / Trivy**                   | Vulnerability scanning in Docker images |
| **AWS Secrets Manager (advanced)** | App secrets in cloud                    |

---

## 🧪 **Testing, Linting, and Code Quality**

| Tool                     | Purpose                                              |
| ------------------------ | ---------------------------------------------------- |
| **Flake8 / Pytest**      | Python linting & unit testing                        |
| **ESLint / Jest**        | JS/TS lint + test                                    |
| **Cypress / Playwright** | E2E frontend testing (CI integrated)                 |
| **Coverage tools**       | Enforce test % policies (e.g. coverage.py, Istanbul) |

---

## 🔔 **Notifications & Monitoring**

| Tool                              | Use                                |
| --------------------------------- | ---------------------------------- |
| **Telegram Bot / Slack Webhooks** | Real-time pipeline status          |
| **GitHub Webhooks**               | Trigger external tools from CI     |
| **CloudWatch / GitHub Logs**      | Monitoring & failure investigation |

---

## 📚 Bonus Tools (Optional but Strong to Learn)

| Tool                     | Use                                       |
| ------------------------ | ----------------------------------------- |
| **Serverless Framework** | Lambda deploys via CI                     |
| **Ansible**              | Agentless config mgmt (e.g., EC2 setup)   |
| **Makefiles**            | Script orchestration inside repos         |
| **AWS CDK (TypeScript)** | Infra-as-code with actual code (optional) |

---

## 💡 Tip

You **don’t have to master every tool at once**. We layer them gradually, making sure by the end of 30 days, you can confidently:

* Build pipelines from scratch
* Deploy containers and infrastructure
* Debug broken builds
* Automate secure, fast releases
* Talk like a pro in interviews 🔥

---
