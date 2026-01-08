import streamlit as st
import pandas as pd

# App title
st.title("📊 TCS Employee Analyzer ")

# Upload CSV file
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Replace Medal text with emoji
    medal_map = {
        "Gold": "🥇",
        "Silver": "🥈",
        "Bronze": "🥉",
        "None": "❌"
    }

    if "Medal" in df.columns:
        df["Medal"] = df["Medal"].map(medal_map).fillna("❌")

    # Display dataset
    st.subheader("📄 Employee Data")
    st.dataframe(df)

    # Basic Insights
    st.subheader("📈 Basic Insights")
    avg_salary = df["Salary"].mean()
    max_salary = df["Salary"].max()
    min_salary = df["Salary"].min()
    avg_experience = df["Experience"].mean()

    st.write(f"**Average Salary:** {avg_salary:.2f}")
    st.write(f"**Highest Salary:** {max_salary}")
    st.write(f"**Lowest Salary:** {min_salary}")
    st.write(f"**Average Experience (Years):** {avg_experience:.2f}")

    # Filter options
    st.subheader("🎯 Filter Employees")

    # Filter by Department
    departments = df["Department"].unique()
    selected_dept = st.selectbox("Select Department", ["All"] + list(departments))
    if selected_dept != "All":
        df_filtered = df[df["Department"] == selected_dept]
    else:
        df_filtered = df

    # Filter by Grade
    grades = df["Grade"].unique()
    selected_grade = st.selectbox("Select Grade", ["All"] + list(grades))
    if selected_grade != "All":
        df_filtered = df_filtered[df_filtered["Grade"] == selected_grade]

    # Show filtered data
    st.subheader("📄 Filtered Employee Data")
    st.dataframe(df_filtered)

    # Bar chart for Salary
    st.subheader("💰 Salary Bar Chart")
    st.bar_chart(df_filtered.set_index("Name")["Salary"])

    # Bar chart for Experience
    st.subheader("🕒 Experience Bar Chart")
    st.bar_chart(df_filtered.set_index("Name")["Experience"])

    # Medal distribution
    st.subheader("🏅 Medal Distribution")
    medal_counts = df_filtered["Medal"].value_counts()
    st.bar_chart(medal_counts)


