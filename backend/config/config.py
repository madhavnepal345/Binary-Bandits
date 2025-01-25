from urllib.parse import quote_plus

username="nepalmadhav32454"
password="M@dh@v2020@"



encoded_username=quote_plus(username)
encoded_password=quote_plus(password)

MONGO_URI = (f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.jbm3k.mongodb.net/")

DB_NAME = "hackathone"
COLLECTION_NAME = "student"
USER_QUESTIONS_COLLECTION="asked_questions"
