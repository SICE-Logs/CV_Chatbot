# 📄 CV Chatbot

An AI-powered CV Analysis and Question Answering system that extracts information from handwritten or digital CVs and allows users to interact with the document using natural language.

## Features

- 📷 OCR-based text extraction from CV images
- 📄 PDF and multi-page PDF support
- 🤖 AI-powered CV question answering using Google Gemini
- 📝 Automatic CV summary generation
- 💾 Download extracted OCR text
- 📥 Download generated CV summaries
- ⚡ Cached OCR processing for improved performance
- 🛡️ Error and exception handling for invalid files and OCR failures

## Tech Stack

- Python 3.10+
- Streamlit
- EasyOCR
- Google Gemini API
- PyMuPDF (PDF processing)
- OpenCV
- Python Dotenv

## Project Structure

```text
cv-chatbot/
│
├── app.py
├── chatbot.py
├── config.py
├── ocr.py
├── rag.py
│
├── uploads/
├── tests/
│
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/SICE-Logs/CV_Chatbot
cd cv-chatbot
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API

Create a `.env` file in the project root (Or simply rename the .env.example file):

```env
GEMINI_API_KEY=your_api_key_here
```


### 5. Run the application

```bash
python -m streamlit run app.py
```



## App Preview

<img width="1473" height="692" alt="image" src="https://github.com/user-attachments/assets/9059a449-6b03-46e2-98e1-32899197596d" />


<img width="1919" height="988" alt="image" src="https://github.com/user-attachments/assets/12e41252-c443-4722-a876-0d254efc6cef" />



## Usage

1. Upload a CV image (`jpg`, `jpeg`, `png`) or PDF.
2. Wait for OCR extraction.
3. Review the extracted text.
4. Generate a structured CV summary.
5. Ask questions about the CV using natural language.
6. Download OCR text or generated summaries.

## Example Questions

- What is the candidate's name?
- What skills does the candidate have?
- What is the candidate's email address?
- Summarize the candidate's education.
- What awards has the candidate received?

## Known Limitations

- OCR accuracy depends on image quality and handwriting readability.
- Extremely stylized handwriting may produce imperfect extraction.
- Gemini API key is required for summary generation and question answering.

## Future Improvements

- Retrieval-Augmented Generation (RAG)
- FAISS vector search
- Enhanced handwriting recognition
- CV skill matching and ranking
- Support for additional document formats

## Author

- Logajit S (Developer)
- Manellore Kusuma Keerthi (Comprehensive App Tester)
- Developed as an AI-powered CV Analysis and Question Answering System using OCR and Large Language Models.
