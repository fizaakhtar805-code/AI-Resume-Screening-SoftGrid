# 🤖 AI-Powered Resume Screening System
### SoftGrid Solutions | AI/ML Internship Project

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-red?style=for-the-badge&logo=jupyter)
![Pandas](https://img.shields.io/badge/Pandas-Data-green?style=for-the-badge&logo=pandas)
![Flask](https://img.shields.io/badge/Flask-WebApp-black?style=for-the-badge&logo=flask)

---

## 📌 Project Overview

An **AI-powered Resume Screening System** that automatically analyzes candidate resumes, extracts relevant information, and predicts whether a candidate should be shortlisted for a job role.

This project was developed as part of the **SoftGrid Solutions AI/ML Internship** program, demonstrating skills in:
- 🔍 Data Collection & Research
- 🧹 Data Preprocessing & EDA
- 🤖 Machine Learning Model Development
- 🌐 Flask Web Application (Coming Soon)
- 📝 Project Documentation

---


---

## 📁 Project Structure

```
AI-Resume-Screening-SoftGrid/
│
├── 📂 Day1/
│   ├── Project Proposal.docx        # Project proposal document
│   ├── Research Summary.docx        # ATS research summary
│   └── ai_resume_screening.csv      # Raw dataset
│
├── 📂 Day2/
│   ├── Task2_Preprocessing.ipynb    # Data cleaning & EDA notebook
│   ├── cleaned_resume_screening.csv # Cleaned dataset
│   └── Screenshots/                 # EDA visualization charts
│
├── 📂 Day3/
│   ├── Task3_ModelDevelopment.ipynb # ML model training notebook
│   ├── confusion_matrices.png       # Confusion matrix for all models
│   ├── feature_importance.png       # Feature importance chart
│   ├── model_accuracy_comparison.png# Accuracy comparison chart
│   ├── model_f1_comparison.png      # F1 score comparison chart
│   ├── Accuracy_Report.docx         # Detailed accuracy report
│   ├── Model_Comparison_Report.docx # Model comparison report
│   └── Performance_Comparison_Document.docx
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
| `education_level` | Education level (0=High School to 3=PhD) |
| `project_count` | Number of projects completed |
| `resume_length` | Length of the resume |
| `github_activity` | GitHub contribution activity score |

---

## 🤖 Machine Learning Models

Four classification models were trained and evaluated:

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| ✅ **Logistic Regression** | **90.02%** | **0.9260** | 0.9307 | **0.9283** |
| 🌲 Random Forest | 89.85% | 0.9232 | **0.9314** | 0.9273 |
| 🌳 Decision Tree | 88.32% | 0.9170 | 0.9146 | 0.9158 |
| 📊 Naive Bayes | 87.00% | **0.9501** | 0.8580 | 0.9017 |

### 🏆 Best Model: Logistic Regression (90.02% Accuracy)

---

## 📈 Key Findings

### Feature Importance (Random Forest)
```
years_experience    ████████████████████  29.1% — Most Important!
github_activity     ████████████████      24.1%
project_count       ███████████           16.1%
skills_match_score  ██████████            15.4%
resume_length       ████████              12.1%
education_level     ██                     3.2% — Least Important
```

> 💡 **Insight:** Experience and GitHub activity together drive **53%** of the shortlisting decision. Education level matters the least — practical skills beat formal qualifications!

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
| Jupyter Notebook | Development environment |
| Anaconda | Python distribution |
| Flask *(Day 4)* | Web application framework |

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.x
- Anaconda (recommended)
- Jupyter Notebook

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/fizaakhtar805-code/AI-Resume-Screening-SoftGrid.git

# 2. Navigate to the project folder
cd AI-Resume-Screening-SoftGrid

# 3. Install required libraries
pip install pandas numpy matplotlib seaborn scikit-learn joblib

# 4. Launch Jupyter Notebook
jupyter notebook
```

---

## 🚀 How to Run

**Day 2 — Preprocessing:**
1. Open `Day2/Task2_Preprocessing.ipynb`
2. Run all cells to clean and explore the dataset

**Day 3 — Model Training:**
1. Open `Day3/Task3_ModelDevelopment.ipynb`
2. Make sure `cleaned_resume_screening.csv` is in the same folder
3. Run all cells to train models and generate results

---

## 📅 Project Progress

| Day | Task | Status |
|-----|------|--------|
| Day 1 | Dataset Collection & Project Research | ✅ Complete |
| Day 2 | Data Preprocessing & EDA | ✅ Complete |
| Day 3 | Machine Learning Model Development | ✅ Complete |
| Day 4 | Flask Web Application | 🔄 In Progress |
| Day 5 | Integration, Testing & Documentation | ⏳ Upcoming |

---

## 🔮 Future Improvements

- 🌐 Deploy the Flask web app to a cloud platform (Heroku / Render)
- 📄 Add support for actual PDF/DOCX resume parsing
- 🧠 Experiment with deep learning models (BERT, transformers)
- 📊 Add a real-time dashboard for HR managers
- 🔍 Implement NLP for extracting skills from raw resume text

---

## 📜 License

This project was developed for educational purposes as part of the SoftGrid Solutions AI/ML Internship Program.

---


