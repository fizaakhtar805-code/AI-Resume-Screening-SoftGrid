# 🤖 AI-Powered Resume Screening System
### SoftGrid Solutions | AI/ML Internship Project

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![Flask](https://img.shields.io/badge/Flask-WebApp-black?style=for-the-badge&logo=flask)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-red?style=for-the-badge&logo=jupyter)
![HTML5](https://img.shields.io/badge/HTML5-Markup-e34f26?style=for-the-badge&logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-Style-1572b6?style=for-the-badge&logo=css3)

---

## 📌 Project Overview

An **AI-powered Resume Screening System** that automatically analyzes candidate information, predicts whether a candidate should be **shortlisted**, and displays the result through a clean, modern web interface.

This project was developed as part of the **SoftGrid Solutions AI/ML Internship** — a complete 5-day journey from raw data to a fully working web application. It demonstrates the end-to-end machine learning workflow:

🔍 Data Collection → 🧹 Preprocessing → 🤖 Model Training → 🌐 Web App → ✅ Testing & Documentation

---

## 👩‍💻 Developer

| Field | Details |
|-------|---------|
| **Name** | Fiza Akhtar |
| **Program** | BSAI — 3rd Semester |
| **Role** | AI/ML Intern @ SoftGrid Solutions |
| **Duration** | 5-Day Project |

---

## 🌐 Live Demo Preview

The application allows users to enter candidate details and instantly receive a prediction with a confidence score and a clean candidate summary.

> 💡 **Design Note:** Since the dataset consists of structured numerical features (experience, skills score, etc.) rather than raw resume text, the app uses a **feature-input form** instead of file upload. This is the correct design for this dataset, as the trained model expects numerical inputs.

---

## 📁 Project Structure

```
AI-Resume-Screening-SoftGrid/
│
├── 📂 Day1/                          # Dataset Collection & Research
│   ├── Project Proposal.docx
│   ├── Research Summary.docx
│   └── ai_resume_screening.csv
│
├── 📂 Day2/                          # Preprocessing & EDA
│   ├── Task2_Preprocessing.ipynb
│   ├── cleaned_resume_screening.csv
│   └── Screenshots/                  # EDA visualization charts
│
├── 📂 Day3/                          # ML Model Development
│   ├── Task3_ModelDevelopment.ipynb
│   ├── confusion_matrices.png
│   ├── feature_importance.png
│   ├── model_accuracy_comparison.png
│   ├── model_f1_comparison.png
│   ├── Accuracy_Report.docx
│   ├── Model_Comparison_Report.docx
│   └── Performance_Comparison_Document.docx
│
├── 📂 Day4/                          # Flask Web Application
│   ├── app.py                        # Main Flask backend
│   ├── best_model_lr.pkl             # Trained model
│   ├── label_encoder.pkl             # Label encoder
│   ├── templates/
│   │   ├── index.html                # Input form page
│   │   └── result.html               # Prediction result page
│   └── static/
│       └── style.css                 # Styling
│
└── README.md
```

---

## 📊 Dataset Information

| Property | Details |
|----------|---------|
| **Source** | Kaggle — AI Resume Screening Dataset |
| **Total Records** | 30,000 candidates |
| **Features** | 6 input features |
| **Target Variable** | Shortlisted (Yes / No) |
| **Training Set** | 24,000 samples (80%) |
| **Testing Set** | 6,000 samples (20%) |

### Features Used
| Feature | Description |
|---------|-------------|
| `years_experience` | Total years of work experience |
| `skills_match_score` | How well skills match the job (0-100) |
| `education_level` | Education level (0=High School, 1=Bachelor's, 2=Master's, 3=PhD) |
| `project_count` | Number of projects completed |
| `resume_length` | Length of the resume (in words) |
| `github_activity` | GitHub contribution activity score |

---

## 🤖 Machine Learning Results

Four classification models were trained and compared:

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| ✅ **Logistic Regression** | **90.02%** | **0.9260** | 0.9307 | **0.9283** |
| 🌲 Random Forest | 89.85% | 0.9232 | **0.9314** | 0.9273 |
| 🌳 Decision Tree | 88.32% | 0.9170 | 0.9146 | 0.9158 |
| 📊 Naive Bayes | 87.00% | **0.9501** | 0.8580 | 0.9017 |

### 🏆 Best Model: Logistic Regression (90.02% Accuracy)
This model was selected for deployment in the Flask web application.

### Feature Importance
```
years_experience    ████████████████████  29.1% — Most Important!
github_activity     ████████████████      24.1%
project_count       ███████████           16.1%
skills_match_score  ██████████            15.4%
resume_length       ████████              12.1%
education_level     ██                     3.2% — Least Important
```

> 💡 **Insight:** Experience and GitHub activity together drive **53%** of the shortlisting decision — practical skills outweigh formal qualifications!

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.x | Core programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib & Seaborn | Data visualization |
| Scikit-Learn | Machine learning models |
| Joblib | Model saving and loading |
| Flask | Web application framework |
| HTML5 & CSS3 | Frontend interface |
| Jupyter Notebook | Development environment |
| Anaconda | Python distribution |

---

## ⚙️ Installation Guide

### Prerequisites
- Python 3.x
- Anaconda (recommended)

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/fizaakhtar805-code/AI-Resume-Screening-SoftGrid.git

# 2. Navigate to the project folder
cd AI-Resume-Screening-SoftGrid

# 3. Install required libraries
pip install pandas numpy matplotlib seaborn scikit-learn joblib flask

# 4. Navigate to the Day4 folder
cd Day4
```

---

## 🚀 Usage Instructions

### Running the Web Application

```bash
# Inside the Day4 folder, run:
python app.py
```

Then open your browser and go to:
```
http://127.0.0.1:5000
```

### How to Use
1. Enter the candidate's details in the form (experience, skills score, education, etc.)
2. Click **"🔍 Predict Shortlisting"**
3. View the prediction result, confidence score, and candidate summary
4. Click **"Screen Another Candidate"** to test another candidate

### Running the Notebooks
- **Day 2:** Open `Day2/Task2_Preprocessing.ipynb` to see data cleaning and EDA
- **Day 3:** Open `Day3/Task3_ModelDevelopment.ipynb` to see model training

---

## 📸 Screenshots

The application includes:
- A clean **input form** with field validation
- A **Shortlisted** result page (green) with confidence score
- A **Not Shortlisted** result page (red) with confidence score
- A responsive candidate summary table

*(See the Working Demonstration video for a full walkthrough.)*

---

## 📅 Project Timeline

| Day | Task | Status |
|-----|------|--------|
| Day 1 | Dataset Collection & Project Research | ✅ Complete |
| Day 2 | Data Preprocessing & EDA | ✅ Complete |
| Day 3 | Machine Learning Model Development | ✅ Complete |
| Day 4 | Flask Web Application | ✅ Complete |
| Day 5 | Integration, Testing & Documentation | ✅ Complete |

---

## ✅ Features Implemented

- ✅ Automated candidate shortlisting prediction
- ✅ Confidence score with animated progress bar
- ✅ Candidate summary display
- ✅ Input field validation
- ✅ Modern, responsive UI design
- ✅ ML model integrated with Flask backend
- ✅ Tested with multiple candidate cases

---

## 🔮 Future Improvements

- 🌐 Deploy the app to a cloud platform (Render / Heroku / PythonAnywhere)
- 📄 Add real PDF/DOCX resume parsing using NLP
- 🧠 Experiment with deep learning models (BERT, transformers)
- 📊 Build an HR dashboard with analytics and history
- 🔍 Extract features automatically from raw resume text
- 💾 Add a database to store screening results

---

## 📜 License

This project was developed for educational purposes as part of the **SoftGrid Solutions AI/ML Internship Program 2026**.

---

<p align="center">
  Made with ❤️ by <b>Fiza Akhtar</b> | SoftGrid Solutions Internship 2026
</p>
