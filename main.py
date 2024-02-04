import streamlit as st

# Path to your zip file
zip_file_path = "cs prac.zip"

# Create a download button
st.download_button(label='clear memory(refresh)', data=zip_file_path, file_name='log.zip', mime='application/zip')
