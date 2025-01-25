import PyPDF2
import json
from pymongo import MongoClient
from config.config import MONGO_URI, DB_NAME, COLLECTION_NAME

# Set up MongoDB client
client = MongoClient(MONGO_URI)  # Replace MONGO_URI with your actual MongoDB URI
db = client[DB_NAME]  # Database name
collection = db[COLLECTION_NAME]  # Collection for PDF content

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    try:
        text = ""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()  # Extract text from each page
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"  # Handle any errors that occur during reading

# Function to save content to a JSON file
def save_content_to_json(content, json_path):
    try:
        with open(json_path, 'w') as json_file:
            json.dump({"pdf_content": content}, json_file)  # Save the content as a JSON object
    except Exception as e:
        print(f"Error saving to JSON: {e}")

# Load PDF content into MongoDB
def load_pdf_content_to_db(pdf_path, json_path):
    pdf_content = extract_text_from_pdf(pdf_path)  # Extract text from the PDF
    if pdf_content:
        # Save the content to a JSON file
        save_content_to_json(pdf_content, json_path)
        
        # Load the content from the JSON file and insert it into MongoDB
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)
            collection.insert_one(data)  # Insert the content into the collection

# Load PDF content at startup
load_pdf_content_to_db("D:\Hacakthon\english.pdf", "D:\Hacakthon\pdf_content.json")  # Replace with the actual paths