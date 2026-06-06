import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def ask_cv_question(cv_text, question):
    prompt = f"""
You are a CV analysis assistant.

Answer ONLY using the CV information provided below.

If the answer is not present in the CV, reply exactly:
Information not available in CV

CV:
{cv_text}

Question:
{question}
"""

    response = model.generate_content(prompt)

    return response.text.strip()