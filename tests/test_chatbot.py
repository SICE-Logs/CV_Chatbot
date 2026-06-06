from ocr import extract_text
from chatbot import ask_cv_question

cv_text = extract_text("167261684.jpg")

while True:
    question = input("\nAsk a question (type exit to quit): ")

    if question.lower() == "exit":
        break

    answer = ask_cv_question(cv_text, question)

    print("\nAnswer:")
    print(answer)