import streamlit as st

st.set_page_config(page_title="🧮 Simple Calculator", layout="centered")
st.markdown("<h1 style='text-align: center;'>🧮 Simple Calculator</h1>", unsafe_allow_html=True)

# Center the input fields
col1, col2, col3 = st.columns([2, 1, 2])
with col1:
    num1 = st.number_input("First Number", step=1.0, key="num1")
with col3:
    num2 = st.number_input("Second Number", step=1.0, key="num2")

st.markdown("### Select Operation")

# Operator buttons in a row like a calculator
op_col1, op_col2, op_col3, op_col4 = st.columns(4)
operation = None
with op_col1:
    if st.button("+"):
        operation = "+"
with op_col2:
    if st.button("-"):
        operation = "-"
with op_col3:
    if st.button("×"):
        operation = "*"
with op_col4:
    if st.button("÷"):
        operation = "/"

# Calculation (triggered by operator button)
if operation:
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    st.success(f"Result: {result}")

# Some CSS for a more calculator-like look
st.markdown("""
    <style>
    .stNumberInput input {
        font-size: 1.5em;
        text-align: center;
    }
    .stButton>button {
        font-size: 2em;
        width: 100%;
        height: 3em;
        margin: 0.2em 0;
    }
    </style>
""", unsafe_allow_html=True)
