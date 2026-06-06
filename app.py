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

    if "last_file" not in st.session_state:
            st.session_state.last_file = None
    if "cv_text" not in st.session_state:
        st.session_state.cv_text = None
    
    if "summary" not in st.session_state:
        st.session_state.summary = None
    
    try:
        if uploaded_file.name != st.session_state.last_file:
            st.session_state.summary = None
            with st.spinner("Extracting text from CV..."):
                st.session_state.cv_text = extract_document_text(
                str(file_path)
                )   
            st.session_state.last_file = uploaded_file.name
        
        cv_text = st.session_state.cv_text
            
    
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
    st.sidebar.info(f"""
    Characters extracted: {len(cv_text)}
    Words extracted: {len(cv_text.split())}
    """)
    
    
    
    
    st.download_button(
    label="Download OCR Text",
    data=cv_text,
    file_name="extracted_cv.txt",
    mime="text/plain"
    )

    st.subheader("CV Summary")

    
    if st.button("Generate Summary"):
        try:
            with st.spinner("Generating summary..."):
                st.session_state.summary = generate_cv_summary(cv_text)
        except Exception as e:
            st.error(f"Summary Generation Error: {e}")
            
    if st.session_state.summary:
        st.markdown(st.session_state.summary)

        st.download_button(
        label="Download CV Summary",
        data=st.session_state.summary,
        file_name="cv_summary.txt",
        mime="text/plain"
        )

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