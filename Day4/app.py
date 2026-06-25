# ============================================================
# RESUME SCREENING SYSTEM - FLASK WEB APPLICATION
# Day 4 | Fiza | SoftGrid Solutions Internship
# ============================================================

# Import required libraries
from flask import Flask, render_template, request
import joblib
import numpy as np

# Create the Flask application
app = Flask(__name__)

# Load the trained model and label encoder (from Day 3)
model = joblib.load("best_model_lr.pkl")
label_encoder = joblib.load("label_encoder.pkl")


# ------------------------------------------------------------
# ROUTE 1: Home Page (the input form)
# ------------------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ------------------------------------------------------------
# ROUTE 2: Prediction Page (shows the result)
# ------------------------------------------------------------
@app.route("/predict", methods=["POST"])
def predict():
    # Get the values entered by the user from the form
    years_experience = float(request.form["years_experience"])
    skills_match_score = float(request.form["skills_match_score"])
    education_level = int(request.form["education_level"])
    project_count = int(request.form["project_count"])
    resume_length = int(request.form["resume_length"])
    github_activity = int(request.form["github_activity"])

    # Arrange the input into the format the model expects
    features = np.array([[
        years_experience,
        skills_match_score,
        education_level,
        project_count,
        resume_length,
        github_activity
    ]])

    # Make the prediction
    prediction = model.predict(features)
    prediction_label = label_encoder.inverse_transform(prediction)[0]

    # Get the confidence score (probability)
    probability = model.predict_proba(features)
    confidence = round(np.max(probability) * 100, 1)

    # Prepare a simple summary of the candidate
    education_map = {0: "High School", 1: "Bachelor's", 2: "Master's", 3: "PhD"}
    education_name = education_map.get(education_level, "Unknown")

    summary = {
        "experience": years_experience,
        "skills": skills_match_score,
        "education": education_name,
        "projects": project_count,
        "github": github_activity
    }

    # Send the result to the result page
    return render_template(
        "result.html",
        prediction=prediction_label,
        confidence=confidence,
        summary=summary
    )


# ------------------------------------------------------------
# Run the Flask application
# ------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)