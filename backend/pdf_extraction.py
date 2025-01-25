import fitz  # PyMuPDF
from pymongo import MongoClient
from config.config import MONGO_URI, DB_NAME, COLLECTION_NAME

def extract_text_from_pdf(pdf_path):
    full_content = []  # List to hold all lines of text from the PDF
    
    # Open the PDF file
    with fitz.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf):
            text = page.get_text()  # Extract text from the page
            print(f"Page {page_number + 1} text:\n{text}\n")  # Debug: Print the text of each page
            
            if text:
                lines = text.split('\n')
                full_content.extend(lines)  # Add lines to the full content list
    
    return full_content

def save_content_to_mongo(content):
    # Connect to MongoDB
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    # Create a single document with all content
    document = {
        "content": "\n".join(content)  # Join all lines into a single string
    }
    
    try:
        collection.insert_one(document)
        print("PDF content saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving PDF content: {e}")

def main():
    pdf_path = "D:\Hacakthon\english.pdf"  # Replace with your PDF file path
    pdf_content = extract_text_from_pdf(pdf_path)
    
    if not pdf_content:
        print("No content found in the PDF.")
    else:
        # Save the extracted content to MongoDB
        save_content_to_mongo(pdf_content)

if __name__ == "__main__":
    main()