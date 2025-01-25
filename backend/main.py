from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import openai
from pymongo import MongoClient
import uvicorn
from config.config import MONGO_URI, DB_NAME, COLLECTION_NAME, USER_QUESTIONS_COLLECTION
from pdf_extractor import extract_text_from_pdf,load_pdf_content_to_db

app = FastAPI()

# Set up OpenAI API key
openai.api_key = "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"

# Set up MongoDB client
client = MongoClient(MONGO_URI)
db = client[DB_NAME]  # Database name
user_questions_collection = db[USER_QUESTIONS_COLLECTION]  # Collection for user questions

@app.get("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        user_input = data.get("message", "")
        user_name = data.get("name", "Anonymous")  # Assuming you want to capture the user's name

        if not user_input:
            raise HTTPException(status_code=400, detail="Please provide a message.")

        # Here you would typically retrieve relevant content from your database
        
        relevant_content = ""  # Placeholder for relevant content retrieval

        # Store user input and relevant content in another collection
        user_question_data = {
            "user_name": user_name,
            "user_input": user_input,
            "relevant_content": relevant_content
        }
        user_questions_collection.insert_one(user_question_data)

        # Combine the relevant content with GPT's response
        messages = [
            {"role": "system", "content": "You are an AI-powered learning assistant. Help users with their educational questions."}
        ]
        if relevant_content:
            messages.append({"role": "assistant", "content": f"Relevant information from your materials:\n{relevant_content}"})
        messages.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        reply = response['choices'][0]['message']['content']
        return JSONResponse(content={"response": reply})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)