import streamlit as st
import pandas as pd
import datetime

st.set_page_config(
    page_title="Personal Expense Tracker",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Personal Expense Tracker")
st.write("Upload, filter, analyze and download your expense data.")

uploaded_file = st.file_uploader(
    "Upload expenses.csv",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Date conversion
    df["Date"] = pd.to_datetime(
        df["Date"],
        dayfirst=True,
        errors="coerce"
    )

    # Amount cleaning
    df["Amount"] = (
        df["Amount"]
        .astype(str)
        .str.replace("₹", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
    )

    df["Amount"] = pd.to_numeric(
        df["Amount"],
        errors="coerce"
    )

    # Remove bad rows
    df = df.dropna(subset=["Date", "Amount"])

else:
    st.info("Please upload expenses.csv to get started.")
    st.stop()

# ---------------- SIDEBAR ----------------

st.sidebar.header("Filters")

date_range = st.sidebar.date_input(
    "Select Date Range",
    (
        datetime.date(2024, 1, 1),
        datetime.date(2024, 5, 31)
    )
)

if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2024, 5, 31)

categories = sorted(df["Category"].dropna().unique())

selected_categories = st.sidebar.multiselect(
    "Select Categories",
    categories,
    default=categories
)

if not selected_categories:
    selected_categories = categories

# Filters
filtered_df = df[
    (df["Date"].dt.date >= start_date) &
    (df["Date"].dt.date <= end_date)
]

filtered_df = filtered_df[
    filtered_df["Category"].isin(selected_categories)
]

# ---------------- KPI ----------------

total_spend = filtered_df["Amount"].sum()

transactions = len(filtered_df)

average_transaction = (
    filtered_df["Amount"].mean()
    if transactions > 0 else 0
)

largest_expense = (
    filtered_df["Amount"].max()
    if transactions > 0 else 0
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Spend",
    f"₹{total_spend:,.2f}"
)

col2.metric(
    "Transactions",
    transactions
)

col3.metric(
    "Average Transaction",
    f"₹{average_transaction:,.2f}"
)

col4.metric(
    "Largest Expense",
    f"₹{largest_expense:,.2f}"
)

# ---------------- TABLE ----------------

st.subheader("Filtered Transactions")

st.dataframe(
    filtered_df,
    hide_index=True,
    use_container_width=True
)

# ---------------- DOWNLOAD ----------------

st.download_button(
    "Download Filtered CSV",
    filtered_df.to_csv(index=False),
    file_name=f"expenses_{start_date}_{end_date}.csv",
    mime="text/csv",
    type="primary"
)

# ---------------- CATEGORY CHART ----------------

st.subheader("Spend by Category")

bar_color = st.color_picker(
    "Choose Bar Colour",
    "#3B82F6"
)

category_summary = (
    filtered_df
    .groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(category_summary)

# ---------------- MONTHLY SUMMARY ----------------

st.subheader("Monthly Summary")

monthly_summary = (
    filtered_df
    .assign(
        Month=filtered_df["Date"].dt.month_name()
    )
    .groupby("Month")
    .agg(
        Total_Spend=("Amount", "sum"),
        Transactions=("Amount", "count")
    )
)

st.table(monthly_summary)

# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    f"Muhammed Yaseen | Personal Expense Tracker | {datetime.date.today()}"
)