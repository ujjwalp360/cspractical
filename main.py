import streamlit as st

# Path to your zip file
zip_file_path = "path/to/your/zip_file.zip"

# Create a download button
st.download_button(label='Download Zip File', data=zip_file_path, file_name='your_zip_file.zip', mime='application/zip')
