from pathlib import Path
import easyocr
import fitz  # PyMuPDF
import streamlit as st

# Initialize OCR Reader once
@st.cache_resource
def get_reader():
    return easyocr.Reader(['en'])



def clean_text(text):
    """
    Clean common OCR artifacts.
    """
    replacements = {
        "_": " ",
        "~": "",
        "|": "I"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


def extract_text(image_path):
    """
    Extract text from image files.
    No preprocessing because it reduced
    handwriting recognition accuracy.
    """
    reader = get_reader()
    result = reader.readtext(str(image_path))

    extracted_text = []

    for item in result:
        extracted_text.append(item[1])

    text = "\n".join(extracted_text)

    return clean_text(text)


def extract_text_from_pdf(pdf_path):
    """
    Extract text from multi-page PDFs.
    """
    extracted_text = []

    pdf = fitz.open(pdf_path)

    for page_num in range(len(pdf)):

        page = pdf[page_num]

        # Higher resolution rendering
        pix = page.get_pixmap(
            matrix=fitz.Matrix(2, 2)
        )

        temp_image = f"temp_page_{page_num}.png"

        pix.save(temp_image)

        try:
            page_text = extract_text(temp_image)
            extracted_text.append(page_text)

        finally:
            temp_file = Path(temp_image)

            if temp_file.exists():
                temp_file.unlink()

    return "\n".join(extracted_text)


def extract_document_text(file_path):
    """
    Universal OCR entry point.

    Supports:
    - JPG
    - JPEG
    - PNG
    - PDF
    """
    try: 
        suffix = Path(file_path).suffix.lower()

        if suffix == ".pdf":
            return extract_text_from_pdf(file_path)

        return extract_text(file_path)
    except Exception as e:
        raise RuntimeError(f"OCR processing failed: {e}")