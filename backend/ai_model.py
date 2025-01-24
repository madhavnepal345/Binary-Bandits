from transformers import pipeline
qa_pipeline=pipeline("question-answering",model="distilbert-base-uncased-distilled-squad", tokenizer="distilbert-base-uncased")



def extract_text_from_pdf(pdf_path):
    pdf_document=fitz.open(pdf_path)
    text=""


    for page_num in range(pdf_document.page_count):
        page=pdf_document.load_page(page_num)
        text+= page.get_text()
    return text



def answer_question_from_context(question,context):
    result=qa_pipeline({
        'context':context,
        'question':question
    })
    return result['answer']