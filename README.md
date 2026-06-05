# CV Chatbot

Features:
- Handwritten CV OCR
- Text Extraction
- Question Answering
- RAG using FAISS
- Gemini LLM

Tech Stack:
- Streamlit
- PaddleOCR
- FAISS
- Sentence Transformers
- Gemini


## Setup

git clone <repo>

cd cv-chatbot

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

Create a .env file:

GEMINI_API_KEY=YOUR_KEY

Run:

streamlit run app.py