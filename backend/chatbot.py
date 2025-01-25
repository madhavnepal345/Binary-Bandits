import openai
import PyPDF2
from pymongo import MongoClient, errors
from config.config import MONGO_URI, DB_NAME, COLLECTION_NAME, USER_QUESTIONS_COLLECTION
# Set your OpenAI API key
openai.api_key = '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'  # Replace with your OpenAI API key



# Function to connect to MongoDB
def connect_to_mongo():
    try:
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]
        print("Connected to MongoDB successfully.")
        return collection
    except errors.ConnectionError as e:
        print(f"Could not connect to MongoDB: {e}")
        return None

# Function to extract text from a PDF file
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

# Function to store PDF content in MongoDB
def store_pdf_content(collection, pdf_text):
    if collection is not None:
        try:
            collection.insert_one({"content": pdf_text})
            print("PDF content stored in MongoDB successfully.")
        except errors.PyMongoError as e:
            print(f"Error storing PDF content in MongoDB: {e}")

# Function to retrieve PDF content from MongoDB
def retrieve_pdf_content(collection):
    if collection is not None:
        try:
            document = collection.find_one()
            return document['content'] if document else None
        except errors.PyMongoError as e:
            print(f"Error retrieving PDF content from MongoDB: {e}")
            return None

# Function to chat with OpenAI
def chat_with_gpt(user_input, context):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI-powered learning assistant."},
                {"role": "user", "content": f"{user_input}\n\nContext:\n{context}"}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error communicating with OpenAI: {e}")
        return "I'm sorry, I couldn't process your request at the moment."

# Load your PDF content and store it in MongoDB
pdf_path = "D:\Hacakthon\english.pdf"  # Replace with the path to your PDF file
pdf_text = extract_text_from_pdf(pdf_path)

# Connect to MongoDB
collection = connect_to_mongo()

# Store PDF content if extraction was successful
if pdf_text:
    store_pdf_content(collection, pdf_text)

# Example usage
if __name__ == "__main__":
    print("Welcome to the AI-powered learning assistant chatbot!")
    print("Type 'exit' or 'quit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        # Retrieve PDF content from MongoDB
        # Retrieve data from MongoDB
        documents = collection.find()
        paragraphs = []
        for doc in documents:
            if 'content' in doc:  # Check if 'content' key exists
                paragraphs.append(doc['content'])  # Append the content if it exists
            else:
                print(f"Document missing 'content' field: {doc}")  # Log the document for debugging