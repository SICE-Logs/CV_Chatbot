import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from config import TESTS_DIR
from ocr import extract_text
from chatbot import ask_cv_question

IMAGE_PATH = TESTS_DIR / "sample_cv.jpg"

cv_text = extract_text(str(IMAGE_PATH))

print("\nCV loaded successfully.\n")

while True:

    question = input(
        "Ask a question (type 'exit' to quit): "
    )

    if question.lower() == "exit":
        break

    answer = ask_cv_question(
        cv_text,
        question
    )

    print("\nAnswer:")
    print(answer)
    print("-" * 50)