💼 SkillBridgeAI – AI-Powered Resume Analyzer & Job Recommender


Live Demo Coming Soon 🚀

🧠 Overview
SkillBridgeAI is a full-stack AI-powered web app designed to analyze a user's resume or skill input and:

🎯 Predict suitable job roles

📉 Detect missing skills through gap analysis

📚 Recommend learning resources

📊 Provide interactive visualizations and predictions

Built for rapid prototyping and educational purposes using a clean Pythonic stack.

🛠️ Tech Stack
Layer	Technology
Frontend	Streamlit (Python UI)
Backend	Flask (REST API for model inference)
ML Model	scikit-learn / joblib / custom classifiers
CI/CD	GitHub Actions (auto test & deploy)
Deployment	Streamlit Cloud (UI), Render (Flask API)

📸 Features
✅ Upload resume or enter skills as input

✅ ML-powered job prediction via Flask API

✅ Skill gap detection & feedback

✅ Streamlit-based user dashboard

✅ Easy model integration (joblib support)

✅ CI/CD via GitHub Actions

✅ Modular folder structure and clean architecture

🤖 Machine Learning Model
Input: Resume text or skill set (numerical or categorical)

Output: Job role/domain prediction

Model: Dummy model for now (RandomForest), extendable to LLM or embeddings

Storage: Saved as .pkl via joblib, served via Flask

🔗 Project Structure
bash
Copy
Edit
SkillBridgeAI/
├── flask_api/               # Backend API
│   ├── ml/                  # Trained model files
│   ├── routes/              # API routes
│   └── app.py               # Flask main app
├── streamlit_ui/            # Streamlit frontend
│   └── main.py              # UI and API calls
├── requirements.txt         # Python dependencies
├── README.md                # Project overview
├── .gitignore               # Ignore venv, pycache, etc.
└── .github/workflows/       # CI/CD pipelines
⚙️ CI/CD Pipelines
GitHub Actions handle:

✅ Dependency install & linting

✅ Unit tests (planned)

✅ Deployment on push (Render + Streamlit Cloud)

🚀 Deployment
Frontend (Streamlit): Coming Soon

Backend (Flask API): Coming Soon

📄 License
This project is licensed under the MIT License.

🙌 Acknowledgements
Inspired by OpenAI, Streamlit, Resume.io, and educational AI platforms.
Powered by Python’s ML and web stack.
