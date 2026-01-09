import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Streamlit Calculator",
    page_icon="🧮",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .calculator {
            background-color: Red;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #2c3e50;
        }
        .result {
            font-size: 22px;
            font-weight: bold;
            color: #1e8449;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>🧮 Streamlit Calculator</h1>", unsafe_allow_html=True)

# Calculator layout
with st.container():
    st.markdown('<div class="calculator">', unsafe_allow_html=True)

    num1 = st.number_input("Enter First Number", value=0.0)
    num1 = st.number_input("Enter Second Number", value=0.0)

    operation = st.selectbox(
        "Select Operation",
        ("Addition", "Subtraction", "Multiplication", "Division")
    )
    result = None

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
                st.error("Division by zero is not allowed")

    if result is not None:
        st.markdown(f"<div class='result'>Result : {result}</div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
# Footer
st.markdown(
    "<p style='text-align:center; color:gray;'>Made with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)
