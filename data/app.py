import streamlit as st

from config import UPLOAD_DIR
from ocr import extract_text
from chatbot import ask_cv_question

st.set_page_config(
    page_title="CV Chatbot",
    page_icon="📄",
    layout="wide"
)

st.title("📄 CV Chatbot")

uploaded_file = st.file_uploader(
    "Upload CV",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    file_path = UPLOAD_DIR / uploaded_file.name

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

    with st.spinner("Extracting text..."):
        cv_text = extract_text(str(file_path))

    st.subheader("Extracted Text")

    st.text_area(
        "OCR Output",
        cv_text,
        height=300
    )

    question = st.text_input(
        "Ask a question about the CV"
    )

    if question:

        with st.spinner("Generating answer..."):

            answer = ask_cv_question(
                cv_text,
                question
            )

        st.subheader("Answer")
        st.write(answer)