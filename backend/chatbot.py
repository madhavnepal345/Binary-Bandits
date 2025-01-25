import PyPDF2
from pymongo import MongoClient, errors
from transformers import pipeline
from config.config import MONGO_URI, DB_NAME, COLLECTION_NAME, USER_QUESTIONS_COLLECTION

# Initialize the Hugging Face summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def connect_to_mongo():
    try:
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]
        summary_collection = db[USER_QUESTIONS_COLLECTION]
        print("Connected to MongoDB successfully.")
        return collection, summary_collection
    except errors.ConnectionError as e:
        print(f"Could not connect to MongoDB: {e}")
        return None, None

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        print("PDF text extracted successfully.")
    except FileNotFoundError:
        print(f"Error: The file {pdf_path} was not found.")
        return None
    except PyPDF2.PdfReaderError as e:
        print(f"Error reading PDF file: {e}")
        return None
    return text

def store_pdf_content(collection, pdf_text):
    if collection is not None:
        try:
            collection.insert_one({"content": pdf_text})
            print("PDF content stored in MongoDB successfully.")
        except errors.PyMongoError as e:
            print(f"Error storing PDF content in MongoDB: {e}")

def summarize_text(text):
    try:
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print(f"Error summarizing text: {e}")
        return "I'm sorry, I couldn't summarize the text at the moment."

pdf_path = r"D:\Hacakthon\english.pdf"  
pdf_text = extract_text_from_pdf(pdf_path)

collection, summary_collection = connect_to_mongo()

if pdf_text:
    store_pdf_content(collection, pdf_text)

if __name__ == "__main__":
    print("Welcome to the AI-powered learning assistant chatbot!")
    print("Type 'exit' or 'quit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        # Retrieve all content from the PDF
        documents = collection.find()
        paragraphs = []
        for doc in documents:
            if 'content' in doc:  
                paragraphs.append(doc['content'])  
            else:
                print(f"Document missing 'content' field: {doc}")  

        # Check if user input matches any content
        matched_content = []
        for para in paragraphs:
            if user_input.lower() in para.lower():  # Case insensitive matching
                matched_content.append(para)

        if matched_content:
            # Join matched content for summarization
            relevant_content = " ".join(matched_content)
            summary = summarize_text(relevant_content)
            
            # Store the summary in the new collection
            if summary_collection is not None:
                try:
                    summary_collection.insert_one({"user_input": user_input, "summary": summary})
                    print("Summary stored in MongoDB successfully.")
                except errors.PyMongoError as e:
                    print(f"Error storing summary in MongoDB: {e}")
            else:
                print("Summary collection is not available.")
        else:
            print("No relevant content found for your query.")