# flask_api/app.py

from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load the saved model

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "ml", "model.pkl")
model = joblib.load(model_path)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    value = data.get("value")

    if value is None:
        return jsonify({"error": "Missing 'value' in request"}), 400

    prediction = model.predict([[value]])[0]
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True)
