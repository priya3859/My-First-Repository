import streamlit as st
import pandas as pd

# App title
st.title("📊 Student Marks Analyzer")

# Upload CSV file
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Display dataset
    st.subheader("📄 Student Data")
    st.dataframe(df)

    # Basic Insights
    st.subheader("📈 Basic Insights")
    avg_marks = df["Marks"].mean()
    max_marks = df["Marks"].max()
    min_marks = df["Marks"].min()

    st.write(f"**Average Marks:** {avg_marks:.2f}")
    st.write(f"**Highest Marks:** {max_marks}")
    st.write(f"**Lowest Marks:** {min_marks}")

    # Filter options
    st.subheader("🎯 Filter Students")
    
    # Filter by Name
    names = df["Name"].unique()
    selected_name = st.selectbox("Select Student Name", ["All"] + list(names))
    if selected_name != "All":
        df_filtered = df[df["Name"] == selected_name]
    else:
        df_filtered = df

    # Filter by Grade
    grades = df["Grade"].unique()
    selected_grade = st.selectbox("Select Grade", ["All"] + list(grades))
    if selected_grade != "All":
        df_filtered = df_filtered[df_filtered["Grade"] == selected_grade]

    # Show filtered data
    st.subheader("📄 Filtered Data")
    st.dataframe(df_filtered)

    # Bar chart for Marks
    st.subheader("📊 Student Marks Bar Chart")
    st.bar_chart(df_filtered.set_index("Name")["Marks"])

    # Medal distribution
    st.subheader("🏅 Medal Distribution")
    medal_counts = df_filtered["Medal"].value_counts()
    st.bar_chart(medal_counts)
