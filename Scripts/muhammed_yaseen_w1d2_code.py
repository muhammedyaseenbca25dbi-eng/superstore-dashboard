import streamlit as st
import pandas as pd
st.title("*STUDENT SCORES*📈")
st.header("Class Performance", divider="green")
data={"Name": ['Aisha', 'Bob', 'Clara', 'Deva','Eva', 'Fazal','Grace', 'Haran','Iris','Jaya'],
      "Math": [88, 52, 76, 91, 43, 67, 85, 59, 78, 95],
      "Science": [72, 45, 88, 83, 38, 71, 90, 62, 55, 80],
      "English": [65, 70, 82, 77, 60, 58, 74, 88, 91, 73],
      "Art": [90, 85, 60, 55, 78, 92, 68, 75, 83, 61]}
df= pd.DataFrame (data)
df['Average'] = df[['Math', 'Science', 'English', 'Art']].mean(axis=1). round(1)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Class Average", f"{df['Average'].mean():.1f}")

with col2:
    st.metric("Highest Average", f"{df['Average'].max():.1f}")

with col3:
    st.metric("Lowest Average", f"{df['Average'].min():.1f}")

with col4:
    st.metric(
        "Students ≥ 70",
        f"{(df['Average'] >= 70).sum():.1f}"
    )
st.dataframe(
    df.style.map(
        lambda x: "color: green" if x >= 70 else "color: red",
        subset=["Average"]
    ),
    hide_index=True,
    use_container_width=True
)
top3 = df.sort_values(by="Average", ascending=False).head(3)

top3.index = range(1, 4)

st.table(top3)
summary = {}

for subject in ["Math", "Science", "English", "Art"]:
    summary[subject] = {
        "Minimum Score": int(df[subject].min()),
        "Maximum Score": int(df[subject].max()),
        "Class Mean": round(df[subject].mean(), 1)
    }
st.json(summary)
st.divider()
st.caption(
    "Muhammed Yaseen | Student Performance Dashboard | 04 June 2026"
)