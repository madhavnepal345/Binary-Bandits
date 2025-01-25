from pymongo import MongoClient
from config.config import COLLECTION_NAME, DB_NAME, MONGO_URI
from pdf_extraction import extract_text_from_pdf
from google.cloud import aiplatform 

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Load PDF content once at the sta# Replace with your PDF file path

def get_answer_from_db(question):
    # Search for the answer in the MongoDB collection
    query = {"user_question": {"$regex": question, "$options": "i"}}  # Case-insensitive search
    result = collection.find_one(query)
    if result:
        return result["user_answer"]
    return None  # Return None if no answer is found

def chat_with_gemini(question):
    # Initialize the AI Platform
    PROJECT_ID = 'midyear-arcade-448818-s8'  # Replace with your project ID
    LOCATION = "asia-south1"  # Replace with your location
    MODEL_NAME = "text-bison"  # Replace with your model name

    aiplatform.init(project=PROJECT_ID, location=LOCATION)
    endpoint = aiplatform.Endpoint(MODEL_NAME)

    # Call the Gemini API
    response = endpoint.predict(instance=[{"content": question}])
    return response.predictions[0]['content']  # Adjust based on the actual response structure

def save_user_input(question, answer, user_info):
    document = {
        "user_question": question,
        "user_answer": answer,
        "user_info": user_info
    }
    try:
        collection.insert_one(document)
        print("Data saved successfully")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the Q&A system!")
    
    while True:
        question = input("Please enter your question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            print("Exiting the program.")
            break
        
        # First, try to get an answer from the database
        answer = get_answer_from_db(question)
        
        # If no answer is found in the database, use the Gemini API
        if answer is None:
            print("No answer found in the database. Asking Gemini API...")
            answer = chat_with_gemini(question)
        
        username = input("Please enter your username: ")
        user_info = {"username": username}

        # Save the user input and the answer
        save_user_input(question, answer, user_info)

        print("Answer:", answer)