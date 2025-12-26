import streamlit as st
import pickle
import pandas as pd

model=pickle.load(open("E:/Student performance/models/student_risk_model.pkl","rb"))
features=pickle.load(open("E:/Student performance/models/features.pkl","rb"))

st.title("Student Academic Risk Prediction System (Sri Lanka – Prototype)")
st.write("This application estimates whether a student may be academically at risk based on prior academic indicators and related behavioural and family factors.It is intended as an early warning tool to support academic monitoring,not as a prediction of final examination results.")

st.markdown(
    """
   **Context**:
This system uses historical academic indicators and contextual factors
to identify students who may require additional academic support.

It does not require users to enter term test or final examination marks.

    """
)
st.subheader("Student Information")

sex_label=st.selectbox("Gender",["Male","Female"])
age=st.number_input("Age",min_value=10,max_value=25,value=16)

medu=st.selectbox("Mother's educatonal level",  [
        "No schooling",
        "Primary (Grades 1–5)",
        "Secondary (Up to O/L)",
        "Higher (A/L or above)"
    ])
fedu=st.selectbox("Father's educatonal level",[
        "No schooling",
        "Primary (Grades 1–5)",
        "Secondary (Up to O/L)",
        "Higher (A/L or above)"
    ])

st.subheader("Academic Performance")




failures=st.number_input("Number of past subject failures",min_value=0,max_value=4,value=0)
absences=st.number_input("Number of school absences",min_value=0,value=5)

st.subheader("Learning Environment")

studytime_label=st.selectbox("Weekly Study Time(Outside the school hours)",["< 2 hours","2-5 hours","5-10 hours",">10 hours"])

internet_label=st.radio("Internet at home",["Yes","No"])

goout=st.slider("Frequency of going out with freinds",min_value=1,max_value=5,value=3,help="1=very low ,5=very high")

freetime=st.slider("Amout of free time after school",min_value=1,max_value=5,value=3)

health=st.slider("Current health status",min_value=1,max_value=5,value=3,help="1=very poor ,5=Excellent")

edu_map = {
    "No schooling": 0,
    "Primary (Grades 1–5)": 1,
    "Secondary (Up to O/L)": 2,
    "Higher (A/L or above)": 3
}


sex_map = {"Male": 0, "Female": 1}
studytime_map={"< 2 hours":1,
               "2-5 hours":2,
               "5-10 hours":3,
               ">10 hours":4
               }
internet_map={"Yes":1,"No":0}
inputs={
    "sex":sex_map[sex_label],
    "age":age,
    "failures":failures,
    "absences":absences,
    "studytime":studytime_map[studytime_label],
    "internet":internet_map[internet_label],
    "medu":edu_map[medu],
    "fedu":edu_map[fedu],
    "goout":goout,
    "health":health,
    "freetime":freetime,
}
DEFAULTS={
    "school": 0,
    "address": 1,
    "famsize": 1,
    "Pstatus": 1,
    "Mjob": 3,
    "Fjob": 3,
    "reason": 0,
    "guardian": 0,
    "traveltime": 1,
    "schoolsup": 0,
    "famsup": 1,
    "paid": 0,
    "activities": 0,
    "nursery": 1,
    "higher": 1,
    "romantic": 0,
    "famrel": 3,
    "Dalc": 1,
    "Walc": 1,
}

for feature in features:
    if feature not in inputs:
        inputs[feature]=DEFAULTS.get(feature,0)

input_df=pd.DataFrame([[inputs[f] for f in features]],columns=features)

if st.button("Predict Academic Risk"):
    prediction=model.predict(input_df)[0]
    probability=model.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result")
   
    if prediction ==1:
        st.error(
                f"**Academic Risk: HIGH**\n\n"
                f"Estimated probability of risk: **{probability:.2f}**\n\n"
                "The student may benefit from academic support or intervention."
        )
    else:
        st.success(
            f"**Academic Risk: LOW**\n\n"
            f"Estimated probability of risk: **{probability:.2f}**\n\n"
            "The student is likely to continue performing satisfactorily."
        )
    
st.markdown(
    """
    ---
    **Disclaimer:**  
    This system is a prototype developed for educational and research purposes.
    Predictions should support, not replace, professional academic judgment.
    """
)

