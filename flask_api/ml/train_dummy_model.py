# flask_api/ml/train_dummy_model.py
from sklearn.ensemble import RandomForestClassifier
import joblib

X = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
y = ["Intern", "Junior Developer", "Junior Developer", "Mid Developer", "Mid Developer", 
     "Senior Developer", "Senior Developer", "Data Analyst", "ML Engineer", "AI Researcher"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "flask_api/ml/model.pkl")
print("✅ Dummy model trained and saved.")
