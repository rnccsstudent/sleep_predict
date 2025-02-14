import streamlit as st
import pickle
import numpy as np

# Load Model
with open('sleep_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Sleeping Hours Prediction & Analysis")

# User Inputs
height = st.number_input("Enter your height (feet)", min_value=4.0, max_value=7.0, step=0.1)
weight = st.number_input("Enter your weight (kg)", min_value=30, max_value=150, step=1)
sleep_hours = st.number_input("Enter your current sleeping hours", min_value=3.0, max_value=12.0, step=0.5)

if st.button("Predict & Analyze"):
    # Prediction
    input_data = np.array([[height, weight]])
    predicted_sleep = model.predict(input_data)[0]

    st.subheader(f"Predicted Sleeping Hours: {predicted_sleep:.1f} hours")

    # Analysis
    if sleep_hours < predicted_sleep - 1:
        st.write("⚠️ Your sleeping hours are **less than expected** based on your height and weight.")
        st.write("📌 Try maintaining a **proper sleep schedule** and reducing stress for better health.")
    elif sleep_hours > predicted_sleep + 1:
        st.write("⚠️ Your sleeping hours are **higher than expected**.")
        st.write("📌 Excess sleep can sometimes indicate **fatigue, depression, or poor lifestyle habits**.")
    else:
        st.write("✅ Your sleeping hours are within a healthy range based on your height and weight.")

    # General Recommendations
    st.subheader("General Recommendations:")
    if height > 6.0 and weight > 80:
        st.write("📌 Taller and heavier individuals may require slightly **more rest** due to energy consumption.")
    elif height < 5.5 and weight < 60:
        st.write("📌 Lighter individuals might feel refreshed with **slightly less sleep**.")

    st.write("⚡ Try maintaining **consistent sleep timings** and a balanced diet for optimal health.")
