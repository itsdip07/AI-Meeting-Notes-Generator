import streamlit as st
import requests
import tempfile

st.title("AI Meeting Notes Generator")
st.write("Upload a meeting audio file to generate the transcript.")

uploaded_file = st.file_uploader("Choose a meeting audio file", type=["wav", "mp3", "webm", "mp4"])

if uploaded_file:
    # Save file temporarily
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(uploaded_file.getbuffer())
    temp.close()

    with st.spinner("Uploading & transcribing..."):
        files = {"file": open(temp.name, "rb")}
        response = requests.post("http://localhost:8000/upload", files=files)

    if response.status_code == 200:
        output = response.json()
        st.subheader("Transcript:")
        st.write(output["transcript"]["text"])
    else:
        st.error("Error: Could not get transcript from backend.")
