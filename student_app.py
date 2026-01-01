import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Student App", layout="centered")

# Session state for storing data
if "students" not in st.session_state:
    st.session_state.students = []

# Navigation menu (Tabs)
menu = st.sidebar.radio(
    "Navigation",
    ["Home", "Student Form", "Student Table"]
)

# ---------------- HOME ----------------
if menu == "Home":
    st.title("🏠 Home")
    st.write("Welcome to the Student Management Web App")
    st.write("This app is created using **Python + Streamlit**.")
    st.info("Use the menu on the left to navigate.")

# ---------------- STUDENT FORM ----------------
elif menu == "Student Form":
    st.title("📝 Student Form")

    name = st.text_input("Student Name")
    age = st.number_input("Age", min_value=1, max_value=100)
    course = st.selectbox("Course", ["Python", "Java", "Web Development", "AI/ML"])

    if st.button("Add Student"):
        if name.strip() == "":
            st.warning("Please enter student name")
        else:
            st.session_state.students.append({
                "Name": name,
                "Age": age,
                "Course": course
            })
            st.success("Student added successfully ✅")

# ---------------- STUDENT TABLE ----------------
elif menu == "Student Table":
    st.title("📊 Student Table")

    if len(st.session_state.students) == 0:
        st.warning("No student data available")
    else:
        df = pd.DataFrame(st.session_state.students)
        st.table(df)
