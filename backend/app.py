from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List, Optional
from config.config import MONGO_URI, DB_NAME, COLLECTION_NAME, USER_QUESTIONS_COLLECTION

app = FastAPI()
client = MongoClient(MONGO_URI)
database = client[DB_NAME]
collection = database[COLLECTION_NAME]
summary_collection = database[USER_QUESTIONS_COLLECTION]

class Item(BaseModel):
    id: str
    user_input: Optional[str]  
    summary: Optional[str]  




@app.get("/summaries/", response_model=List[Item])
def get_summaries():
    summaries = []
    for summary in summary_collection.find():
        summary['_id'] = str(summary['_id'])  
        user_input = summary.get('user_input', 'No input provided')  
        summary_text = summary.get('summary', 'No summary available')  
        summaries.append(Item(id=summary['_id'], user_input=user_input, summary=summary_text))
    return summaries

@app.get("/summaries/{summary_id}", response_model=Item)
def get_summary(summary_id: str):
    summary = summary_collection.find_one({"_id": summary_id})
    if summary is None:
        raise HTTPException(status_code=404, detail="Summary not found")
    summary['_id'] = str(summary['_id'])  
    user_input = summary.get('user_input', 'No input provided')  
    summary_text = summary.get('summary', 'No summary available')  
    return Item(id=summary['_id'], user_input=user_input, summary=summary_text)

@app.get("/first-summary/", response_model=Item)
def get_first_summary():
    first_summary = summary_collection.find_one()
    if first_summary is None:
        raise HTTPException(status_code=404, detail="No summaries found")
    first_summary['_id'] = str(first_summary['_id'])  
    user_input = first_summary.get('user_input', 'No input provided')  
    summary_text = first_summary.get('summary', 'No summary available')  
    return Item(id=first_summary['_id'], user_input=user_input, summary=summary_text)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)