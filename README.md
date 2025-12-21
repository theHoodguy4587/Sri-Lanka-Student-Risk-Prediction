# 🎓 Student Academic Risk Prediction (Sri Lanka)

This project predicts whether a secondary school student is at **high academic risk** or **low academic risk** using machine learning.  
It is built using the **Student Performance Dataset** and deployed as an interactive **Streamlit web application**.

The goal is to help identify students who may benefit from early academic support or intervention.

---

## 🚀 Live Application
🔗 *(Add Streamlit Cloud link here after deployment)*  
Example: https://your-app-name.streamlit.app

---

## 📌 Problem Statement

Early identification of students at academic risk allows educators and institutions to:
- Provide timely interventions
- Improve academic outcomes
- Reduce dropout rates

This project uses demographic, family, social, and academic behavior features to predict **academic risk**.

---

## 📊 Dataset

- **Source:** Student Performance Dataset (UCI Machine Learning Repository)
- **Students:** Portuguese secondary school students
- **Target Variable:** Academic Risk (derived from final grade `G3`)
- **Rows:** ~395
- **Features Used:** 30+ student-related attributes

### Examples of Features
- Age, gender, family size
- Parental education and jobs
- Study time, failures, absences
- Alcohol consumption, health
- Internet access, extracurricular activities

> ⚠️ **Important:**  
> Term test scores (`G1`, `G2`) are **excluded** from the final model to avoid data leakage and unrealistically high predictions.

---

## 🧠 Machine Learning Model

- **Algorithm:** Logistic Regression
- **Why Logistic Regression?**
  - Interpretable
  - Suitable for binary classification
  - Performs well on small-to-medium datasets

### Target Definition
```text
Academic Risk = 1 → Final Grade (G3) < 10
Academic Risk = 0 → Final Grade (G3) ≥ 10
