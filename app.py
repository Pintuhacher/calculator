import streamlit as st

st.title("🧮 Simple Calculator")

# Take user inputs
num1 = st.number_input("Enter first number:", step=1.0)
num2 = st.number_input("Enter second number:", step=1.0)

# Operation selection
operation = st.radio("Select Operation:", ["+", "-", "*", "/"])

# Calculate when button is clicked
if st.button("Calculate"):
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
