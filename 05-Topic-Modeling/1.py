import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title and description
st.title("Welcome to My Website")
st.write("This is a simple top-level website built using Streamlit!")

# Navigation bar or Sidebar
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Select a page", ["Home", "About", "Contact"])

# Home Page
if option == "Home":
    st.header("Home Page")
    st.write("This is the home page of the website.")

# About Page
elif option == "About":
    st.header("About Us")
    st.write("This page contains information about us.")

# Contact Page
elif option == "Contact":
    st.header("Contact Us")
    st.write("You can reach us via email at contact@example.com.")

# Footer
st.write("---")
st.write("© 2024 My Website - All rights reserved.")

# Additional Features

# Display an image
st.image("https://via.placeholder.com/150", caption="Sample Image")

# Display a chart
# Create a sample dataframe
df = pd.DataFrame({
    'x': np.random.randn(1000),
    'y': np.random.randn(1000)
})

# Plot the data
fig, ax = plt.subplots()
ax.scatter(df['x'], df['y'])
st.pyplot(fig)

# Display a map
st.map(pd.DataFrame({
    'lat': [37.76, 37.77, 37.78, 37.79],
    'lon': [-122.4, -122.41, -122.42, -122.43]
}))

# Add a file uploader
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write("File uploaded successfully!")

# Additional Streamlit Features

# Display a progress bar
st.write("Progress Bar Example")
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)

# Display a slider
st.write("Slider Example")
slider_value = st.slider("Select a value", 0, 100)
st.write(f"Selected value: {slider_value}")

# Display a text input
st.write("Text Input Example")
text_input = st.text_input("Enter some text")
st.write(f"Entered text: {text_input}")

# Display a checkbox
st.write("Checkbox Example")
checkbox = st.checkbox("Check me!")
if checkbox:
    st.write("Checkbox is checked!")

# Display a radio button
st.write("Radio Button Example")
radio_option = st.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write(f"Selected option: {radio_option}")

# Display a selectbox
st.write("Selectbox Example")
selectbox_option = st.selectbox("Choose an option", ["Option A", "Option B", "Option C"])
st.write(f"Selected option: {selectbox_option}")

# Display a multiselect
st.write("Multiselect Example")
multiselect_options = st.multiselect("Choose options", ["Option 1", "Option 2", "Option 3"])
st.write(f"Selected options: {multiselect_options}")

# Display a date input
st.write("Date Input Example")
date_input = st.date_input("Select a date")
st.write(f"Selected date: {date_input}")

# Display a time input
st.write("Time Input Example")
time_input = st.time_input("Select a time")
st.write(f"Selected time: {time_input}")

# Display a color picker
st.write("Color Picker Example")
color_picker = st.color_picker("Pick a color")
st.write(f"Selected color: {color_picker}")