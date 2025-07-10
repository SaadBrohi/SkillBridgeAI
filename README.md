# 💼 **SkillBridgeAI** – AI-Powered Resume Analyzer & Job Recommender

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Backend CI](https://github.com/Saadbrohi/SkillBridgeAI/actions/workflows/backend.yml/badge.svg)](https://github.com/Saadbrohi/SkillBridgeAI/actions)
[![Frontend CI](https://github.com/Saadbrohi/SkillBridgeAI/actions/workflows/frontend.yml/badge.svg)](https://github.com/Saadbrohi/SkillBridgeAI/actions)

> **SkillBridgeAI** is a full-stack, ML-integrated web application that helps users identify the most suitable job roles based on their skills or resume content. It uses a trained ML model to offer career guidance and learning recommendations.

---

## 🧠 **What It Does**

🚀 **SkillBridgeAI** intelligently:
- 🎯 Predicts job roles based on resume or skills
- 📉 Detects missing skills (gap analysis)
- 📚 Recommends learning resources
- 📊 Presents interactive UI via Streamlit
- 🧠 Integrates a trained ML model with Flask API

---

## 🛠️ **Tech Stack**

| Layer       | Technology                                  |
|-------------|---------------------------------------------|
| 🖥️ Frontend  | **Streamlit** (Python-based UI)             |
| 🔧 Backend   | **Flask** (REST API to serve ML model)      |
| 🧠 Model     | **scikit-learn**, **joblib**                |
| 📦 Database  | Coming Soon (SQLite or PostgreSQL)          |
| 🚀 DevOps    | **GitHub Actions**, CI/CD, Deployment Ready |
| 🌐 Hosting   | Streamlit Cloud (UI) & Render (Backend API) |

---


---

## 🚀 **Key Features**

✅ Upload resume or enter skills manually  
✅ ML-powered job prediction API  
✅ Modular architecture (Flask API + Streamlit UI)  
✅ Skill gap detection (coming soon)  
✅ Realtime frontend-backend interaction  
✅ Docker & deployment ready (coming soon)  
✅ CI/CD via GitHub Actions  

---

## 🤖 **Machine Learning Details**

- **Model:** Random Forest (can be replaced with LLM or custom classifier)
- **Input:** Resume text or skills list
- **Output:** Predicted job domain or title
- **Storage:** `joblib`-serialized `.pkl` file served via Flask
- **Versioning:** Easy swap with newer model versions via `/ml/model.pkl`

---

## 🧪 **API Endpoint**

| Method | Endpoint        | Description           |
|--------|------------------|------------------------|
| POST   | `/predict`       | Accepts JSON input and returns predicted job title |

Example:

```json
POST /predict
{
  "value": 9
}

{
  "prediction": "Data Analyst"
}

---

## **Deployment Plan**

| Component     | Platform         |
| ------------- | ---------------- |
| Frontend (UI) | Streamlit Cloud  |
| Backend (API) | FastAPI |
| CI/CD         | GitHub Actions   |

---

## ⚙️** CI/CD Workflow**
GitHub Actions automate:

🔍 Dependency installation

✅ Code linting and tests (coming)

🚀 Auto-deploy to production after push



💬 Built by Saad Brohi — aspiring AI/ML Engineer
⭐ Star the repo if you like it! Contributions are welcome.
