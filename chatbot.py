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
    try: 
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
    except Exception as e:
        return f"Error generating answer: {str(e)}"

def generate_cv_summary(cv_text: str) -> str:
    try: 
        prompt = f"""
Analyze the following CV and generate a structured summary. Try to correct any OCR errors and inconsistencies 
and extract key information in the following format:

Format:

Name:
Email:
Phone:
Address:
Skills:
Education:
Experience:
Awards:
Other Information:

If a field is missing, write:
Not Available

CV:
{cv_text}
"""

        response = model.generate_content(prompt)

        return response.text.strip()
    except Exception as e:
        return f"Error generating summary: {str(e)}"