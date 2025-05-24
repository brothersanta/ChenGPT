import streamlit as st
import requests

st.title("Text Summarizer")

text_input = st.text_area("Enter text to summarize:")

if st.button("Summarize"):
    response = requests.post(
        "http://localhost:8000/summarize/",
        data={"text": text_input}
    )
    result = response.json()
    st.subheader("Summary")
    st.write(result["summary"])
