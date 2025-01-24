from config.config import COLLECTION_NAME,DB_NAME

from pdf_extrction import extract_text_from_pdf
from gemmine import answer_question_from_context
from aiplatform_client import chat_with_model


def save_user_input(question,answer,user_info):
    document={
        "user_question":question,
        "user_answer":answer,
        "user_info":user_info
    }
    collection.insert_one(document)
    print("Data saved sucessfully")
