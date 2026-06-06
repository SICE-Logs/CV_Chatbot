import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from ocr import extract_text
from chatbot import ask_cv_question

cv_text = extract_text("167261684.jpg")

print("\nCV loaded successfully.\n")

while True:
    question = input("Ask a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    answer = ask_cv_question(cv_text, question)

    print("\nAnswer:")
    print(answer)
    print("-" * 50)