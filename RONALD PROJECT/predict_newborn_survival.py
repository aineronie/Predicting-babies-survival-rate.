import streamlit as st
import pandas as pd
import pickle

# Load the trained model pipeline
with open("RateOfDeath.pkl", "rb") as f:
    model = pickle.load(f)

# App title
st.title("🍼 Neonatal Mortality Prediction App")
st.write("Predict whether a newborn is likely to survive or die within the first 28 days based on clinical and maternal data.")

# User Input
st.header("Enter Baby and Maternal Details")

age = st.number_input("Mother's Age", min_value=10, max_value=50)
gravida = st.number_input("Gravida", min_value=1)
parity = st.number_input("Parity", min_value=0)
gestation_age = st.number_input("Gestation Age (weeks)", min_value=20, max_value=45)
term_preterm = st.selectbox("Term/Preterm", ['Term', 'Preterm'])
hiv_status = st.selectbox("HIV Status", ['Negative', 'Positive'])
mode_of_delivery = st.selectbox("Mode of Delivery", ['SVD', 'C-Section', 'Breech', 'Vacuum'])
agpar_1min = st.slider("AGPAR Score at 1 Minute", 0, 10)
agpar_5min = st.slider("AGPAR Score at 5 Minutes", 0, 10)
sex_of_baby = st.selectbox("Sex of Baby", ['Male', 'Female'])
weight = st.number_input("Birth Weight (grams)", min_value=500, max_value=6000)
pnc_6hrs = st.selectbox("PNC at 6 Hours", ['Yes', 'No'])
pnc_24hrs = st.selectbox("PNC at 24 Hours", ['Yes', 'No'])

# Encode input to match model expectations
def encode_input():
    delivery_map = {'SVD': 0, 'C-Section': 1, 'Breech': 2, 'Vacuum': 3}
    return pd.DataFrame({
        'AGE': [age],
        'GRAVIDA': [gravida],
        'PARITY': [parity],
        'GESTATION AGE': [gestation_age],
        'TERM/PRETERM': [1 if term_preterm == 'Term' else 0],
        'HIV STATUS': [1 if hiv_status == 'Positive' else 0],
        'MODE OF DELIVERY': [delivery_map[mode_of_delivery]],
        'AGPAR SCORE(1MIN)': [agpar_1min],
        'AGPAR SCORE(5MIN)': [agpar_5min],
        'SEX OF BABY': [1 if sex_of_baby == 'Male' else 0],
        'WEIGHT': [weight / 1000],  # Convert grams to kg
        'PNC AT 6 HRS': [1 if pnc_6hrs == 'Yes' else 0],
        'PNC AT 24 HRS ': [1 if pnc_24hrs == 'Yes' else 0]
    })

# Predict button
if st.button("Predict Survival"):
    input_data = encode_input()

    # Optional: show the input for debugging
    # st.write("Model Input Preview:", input_data)

    try:
        prediction = model.predict(input_data)[0]
        prediction_proba = model.predict_proba(input_data)[0][1]

        if prediction == 1:
            st.error(f"❌ Prediction: Baby is at risk of death.\nProbability: {prediction_proba:.2f}")
        else:
            st.success(f"✅ Prediction: Baby is likely to survive.\nProbability: {prediction_proba:.2f}")
    except Exception as e:
        st.error(f"⚠️ An error occurred during prediction: {e}")
