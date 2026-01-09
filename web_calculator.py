import streamlit as st

# App title
st.title("Simple Calculator")

# User inputs
num1 = st.number_input("Enter first number", value=0)
num2 = st.number_input("Enter second number", value=0)

# Select operation
operation = st.selectbox(
    "Choose an operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Show result on button click
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero!"
    st.write("Result:", result)


