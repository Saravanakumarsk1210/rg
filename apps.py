import streamlit as st
import random

def generate_random_number(start, end):
    return random.randint(start, end)

def main():
    st.title("Random Number Generator")

    # User input for the range
    from_value = st.number_input("From:", min_value=float('-1.797e+308'), max_value=float('1.797e+308'), key='from_value')
    to_value = st.number_input("To:", min_value=float('-1.797e+308'), max_value=float('1.797e+308'), key='to_value')

    # Generate button
    if st.button("Generate"):
        if from_value <= to_value:
            random_number = generate_random_number(int(from_value), int(to_value))
            st.success(f"Random Number: {random_number}")
        else:
            st.error("Error: 'From' value must be less than or equal to 'To' value.")

if __name__ == "__main__":
    main()
