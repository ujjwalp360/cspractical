import streamlit as st
import base64

# Path to your zip file
zip_file_path = "cs prac.zip"

# Function to read the contents of the zip file
def read_zip_file(zip_file_path):
    with open(zip_file_path, "rb") as f:
        zip_data = f.read()
    return zip_data

# Read the contents of the zip file
zip_data = read_zip_file(zip_file_path)

# Create a download button
b64 = base64.b64encode(zip_data).decode()
href = f'<a href="data:application/zip;base64,{b64}" download="your_zip_file.zip">Download Zip File</a>'
st.markdown(href, unsafe_allow_html=True)
