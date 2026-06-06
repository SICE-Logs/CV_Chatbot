import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-flash-latest")

def ask_cv_question(cv_text: str, question: str) -> str:
    prompt = f"""
You are a CV analysis assistant.

Rules:
1. Answer ONLY from the CV.
2. Do not make assumptions.
3. If the answer is not found, reply exactly:
Information not available in CV

CV:
{cv_text}

Question:
{question}
"""

    response = model.generate_content(prompt)

    return response.text.strip()