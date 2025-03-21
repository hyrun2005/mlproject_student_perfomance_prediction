# 🎓 Student Performance Prediction – End-to-End ML Project

This repository contains an end-to-end machine learning project aimed at predicting student performance using various ML algorithms. The project includes data preprocessing, model training (CatBoost, XGBoost, etc.), evaluation, and deployment through a simple Flask web application.

---

## 🚀 Project Features

- 📊 Exploratory Data Analysis (EDA)
- 🧼 Data preprocessing and transformation
- 🤖 ML models: CatBoost, XGBoost, Random Forest, etc.
- 🔁 Model evaluation and selection
- 💾 Artifact and model storage
- 🌐 Flask web application for predictions

---

## 🌍 Live Demo

You can try the web application here:  
👉 [Click to Open](http://student-perfomance-env.eba-rwgxqhmh.us-east-1.elasticbeanstalk.com/prediction_data)

---

## 📂 Code Overview

- `application.py` – Main Flask app for handling web UI and predictions.
- `requirements.txt` – List of required Python libraries.
- `src/components/` – Modular scripts for data ingestion, transformation, model training, and evaluation.
- `src/pipeline/` – Handles training and prediction workflows.
- `src/utils.py` – Utility functions (e.g., saving/loading models).
- `src/logger.py` – Logging mechanism.
- `templates/` – HTML files for the web interface.
- `notebook/` – Jupyter notebooks used during development and testing.
- `artifacts/` – Folder where trained models and data transformers are saved.

---

## 🛠 Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/hyrun2005/mlproject_student_perfomance_prediction.git
cd mlproject_student_perfomance_prediction
pip install -r requirements.txt
```
---

## ML Libraries Used
- pandas, numpy
- scikit-learn
- catboost
- xgboost
- matplotlib, seaborn
- dill
- Flask
---
## 💡 How to Use
Run the training pipeline using the code in src/.
Launch the web app:
bash
Copy
Edit
python application.py
Open the browser to enter student data and receive predictions.
🧑‍💻 Author
Yurii Hyrun

