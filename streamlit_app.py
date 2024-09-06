# streamlit_user_input_random_name.py

import streamlit as st
import random

# Title of the app
st.title("Random Name Selector")

# Add a description
st.write("This app lets you enter a list of names and then randomly selects one.")

# Input for names from the user (each name separated by a comma)
names_input = st.text_area("Enter names separated by commas:")

# Button to trigger random name selection and word count
if st.button("Select Random Name"):
    # Split the names by commas and strip whitespace
    names_list = [name.strip() for name in names_input.split(",") if name.strip()]

    if names_list:
        # Select a random name from the list
        selected_name = random.choice(names_list)
    
        
        # Display the random name and word count
        st.write(f"Randomly Selected Name: {selected_name}")
    else:
        st.write("Please enter at least one name.")
else:
    st.write("Enter names and text, then click the button to proceed.")
