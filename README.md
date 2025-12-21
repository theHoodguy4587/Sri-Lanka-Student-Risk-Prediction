# 🎓 Student Academic Risk Prediction (Sri Lanka)

This project predicts whether a secondary school student is at **high academic risk** or **low academic risk** using machine learning.
It is built using the **Student Performance Dataset** and deployed as an interactive **Streamlit web application**.

The goal is to help identify students who may benefit from early academic support or intervention.

---

## 🚀 Live Application

🔗 *(Add Streamlit Cloud link here after deployment)*
Example: [https://your-app-name.streamlit.app]()

---

## 📌 Problem Statement

Early identification of students at academic risk allows educators and institutions to:

* Provide timely interventions
* Improve academic outcomes
* Reduce dropout rates

This project uses demographic, family, social, and academic behavior features to predict **academic risk**.

---

## 📊 Dataset

* **Source:** Student Performance Dataset (UCI Machine Learning Repository)
* **Students:** Portuguese secondary school students
* **Target Variable:** Academic Risk (derived from final grade `G3`)
* **Rows:** ~395
* **Features Used:** 30+ student-related attributes

### Examples of Features

* Age, gender, family size
* Parental education and jobs
* Study time, failures, absences
* Alcohol consumption, health
* Internet access, extracurricular activities

> ⚠️ **Important:**
> Term test scores (`G1`, `G2`) are **excluded** from the final model to avoid data leakage and unrealistically high predictions.

---

## 🧠 Machine Learning Model

* **Algorithm:** Logistic Regression
* **Why Logistic Regression?**

  * Interpretable and easy to explain
  * Suitable for binary classification
  * Performs well on small-to-medium datasets

### 🎯 Target Definition

```
Academic Risk = 1  → Final Grade (G3) < 10
Academic Risk = 0  → Final Grade (G3) ≥ 10
```

---

## ⚙️ Tech Stack

| Component         | Technology    |
| ----------------- | ------------- |
| Language          | Python        |
| ML Library        | scikit-learn  |
| Data Handling     | pandas, numpy |
| Visualization     | matplotlib    |
| Web App           | Streamlit     |
| Model Persistence | pickle        |
| Version Control   | Git & GitHub  |

---

## 📂 Project Structure

```
Student-Risk-Prediction/
│
├── app.py                  # Streamlit web application
├── train_model.py          # Model training script
├── student_risk_model.pkl  # Trained ML model
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
└── data/
    └── student.csv         # Dataset
```

---

## 🖥️ Streamlit Application Features

* User-friendly input form
* Real-time academic risk prediction
* Probability-based output
* Clear academic guidance message

### Example Output

```
Academic Risk: HIGH
Estimated Probability of Risk: 0.73
The student may benefit from academic support or intervention.
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/theHoodguy4587/Sri-Lanka-Student-Risk-Prediction.git
cd Sri-Lanka-Student-Risk-Prediction
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App

```bash
streamlit run app.py
```

---

## 📦 Deployment (Streamlit Cloud)

1. Push the project to **GitHub**
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Select `app.py` as the main file
5. Click **Deploy** 🎉

---

## 📈 Future Improvements

* Add feature importance visualization
* Use ensemble models (Random Forest, XGBoost)
* Handle class imbalance
* Add model monitoring
* Deploy with Docker

---

## 👤 Author

**Senitha Gunathilaka**
Data Science Student
Interested in Machine Learning, Analytics, and MLOps

🔗 GitHub: [https://github.com/theHoodguy4587](https://github.com/theHoodguy4587)

---

## 📜 License

This project is for **educational and research purposes only**.
