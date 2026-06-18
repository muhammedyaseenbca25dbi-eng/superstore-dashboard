import streamlit as st

# Page title
st.title("🏋️ Health & Fitness Calculator")
st.markdown("Calculate BMI, daily calorie needs, and ideal weight range.")
st.markdown("---")

# User Inputs
st.header("Personal Details")

name = st.text_input("Name")
age = st.number_input("Age", min_value=10, max_value=100, value=20)

sex = st.radio(
    "Sex",
    ["Male", "Female"],
    horizontal=True
)

weight = st.slider(
    "Weight (kg)",
    min_value=30.0,
    max_value=150.0,
    value=70.0,
    step=0.5
)

height = st.slider(
    "Height (cm)",
    min_value=100,
    max_value=220,
    value=170,
    step=1
)

st.write(
    f"Name: {name}, Age: {age}, Sex: {sex}, Weight: {weight} kg, Height: {height} cm"
)

# BMI Section
st.header("BMI Calculator")

bmi = weight / ((height / 100) ** 2)
bmi = round(bmi, 1)

st.metric("BMI", bmi)

if bmi < 18.5:
    st.warning(f"Underweight | Health Risk: Moderate")
    bmi_class = "Underweight"
elif bmi < 25:
    st.success(f"Normal Weight | Health Risk: Low")
    bmi_class = "Normal Weight"
elif bmi < 30:
    st.warning(f"Overweight | Health Risk: Elevated")
    bmi_class = "Overweight"
else:
    st.error(f"Obese | Health Risk: High")
    bmi_class = "Obese"

# Daily Calorie Need
st.header("Daily Calorie Need")

activity_options = {
    "Sedentary (desk job)": 1.2,
    "Lightly active (1–3 days/wk)": 1.375,
    "Moderately active (3–5 days)": 1.55,
    "Active (6–7 days)": 1.725,
    "Very active (twice/day training)": 1.9
}

activity = st.selectbox(
    "Activity Level",
    list(activity_options.keys())
)

multiplier = activity_options[activity]

# BMR Calculation
if sex == "Male":
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
else:
    bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

daily_calories = round(bmr * multiplier)

st.metric("Daily Calories Needed", f"{daily_calories} kcal")

# Ideal Weight Range
st.header("Ideal Weight Range")

if sex == "Male":
    ideal_weight = 52 + 1.9 * ((height / 2.54) - 60)
else:
    ideal_weight = 49 + 1.7 * ((height / 2.54) - 60)

low_weight = round(ideal_weight * 0.9, 1)
high_weight = round(ideal_weight * 1.1, 1)

col1, col2 = st.columns(2)

with col1:
    st.metric("Low Range", f"{low_weight} kg")

with col2:
    st.metric("High Range", f"{high_weight} kg")

# Summary
st.header("Full Summary")

if st.button("Show my summary"):
    st.write(f"👤 Name: {name}")
    st.write(f"📊 BMI: {bmi} ({bmi_class})")
    st.write(f"🔥 Daily Calories: {daily_calories} kcal")
    st.write(f"⚖️ Ideal Weight Range: {low_weight} kg - {high_weight} kg")