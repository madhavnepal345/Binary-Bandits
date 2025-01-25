import PyPDF2
import json
from pymongo import MongoClient
from config.config import MONGO_URI, DB_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)  
db = client[DB_NAME]  
collection = db[COLLECTION_NAME]  

def extract_text_from_pdf(pdf_path):
    try:
        text = ""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()  
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"  

def save_content_to_json(content, json_path):
    try:
        with open(json_path, 'w') as json_file:
            json.dump({"pdf_content": content}, json_file)  
    except Exception as e:
        print(f"Error saving to JSON: {e}")

def load_pdf_content_to_db(pdf_path, json_path):
    pdf_content = extract_text_from_pdf(pdf_path)  
    if pdf_content:
        save_content_to_json(pdf_content, json_path)
        
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)
            collection.insert_one(data)  

load_pdf_content_to_db("D:\Hacakthon\english.pdf", "D:\Hacakthon\pdf_content.json")  