import streamlit as st
# Title
st.title("Hello, World!")
st.write("Welcome to the Python Class at Governor House.")

# Simple Input Box
name = st.text_input("Enter Your Name:", "Type Here")
day = st.text_input("Enter Your Day:", "Type Here")
teacher = st.text_input("Enter Your Teacher Name:", "Type Here")

# Button to display a Greeting Message
if st.button("Submit"):
    st.write(f"Hello, {name}! Welcome to the Python Class on {day}, which will be conducted by Sir {teacher}.")
