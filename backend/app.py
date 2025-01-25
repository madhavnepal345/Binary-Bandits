from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List, Optional
from config.config import MONGO_URI, DB_NAME, COLLECTION_NAME

app = FastAPI()
client = MongoClient(MONGO_URI)
database = client[DB_NAME]
collection = database[COLLECTION_NAME]

class Item(BaseModel):
    id: str
    name: Optional[str]  
    description: Optional[str]  

@app.get("/items/", response_model=List[Item])
def get_items():
    items = []
    for item in collection.find():
        item['_id'] = str(item['_id'])  
        name = item.get('name', 'Unnamed Item')  
        description = item.get('description', 'No description available')  
        items.append(Item(id=item['_id'], name=name, description=description))
    return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: str):
    item = collection.find_one({"_id": item_id})
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    item['_id'] = str(item['_id'])  
    name = item.get('name', 'Unnamed Item')  
    description = item.get('description', 'No description available')  
    return Item(id=item['_id'], name=name, description=description)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)