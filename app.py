import streamlit as st

from chatbot import ask_cv_question, generate_cv_summary
from config import UPLOAD_DIR

from ocr import extract_document_text
from chatbot import ask_cv_question

st.set_page_config(
    page_title="CV Chatbot",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Handwritten CV Chatbot")

uploaded_file = st.file_uploader(
    "Upload a CV",
    type=["jpg", "jpeg", "png","pdf"]
)

if uploaded_file:

    file_path = UPLOAD_DIR / uploaded_file.name

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("CV uploaded successfully!")

    try:


        with st.spinner("Extracting text from CV..."):
            cv_text = extract_document_text(str(file_path))
    
    except Exception as e:
        st.error(f"OCR Error: {e}")
        st.stop()
    
    if not cv_text.strip():
        st.error("No text extracted from the CV. Please check the file and try again.")
        st.stop()

    st.subheader("Extracted Text")

    st.text_area(
        "OCR Output",
        cv_text,
        height=300
    )
    st.subheader("CV Summary")

    if "summary" not in st.session_state:
        st.session_state.summary = None

    if st.button("Generate Summary"):
        try:
            with st.spinner("Generating summary..."):
                st.session_state.summary = generate_cv_summary(cv_text)
        except Exception as e:
            st.error(f"Summary Generation Error: {e}")
            
    if st.session_state.summary:
        st.markdown(st.session_state.summary)

    st.subheader("Ask Questions")

    question = st.text_input(
        "Enter your question"
    )

    if question:

        with st.spinner("Generating answer..."):

            answer = ask_cv_question(
                cv_text,
                question
            )

        st.subheader("Answer")
        st.success(answer)