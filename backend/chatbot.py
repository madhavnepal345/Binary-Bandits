import os
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from pymongo import MongoClient
import tensorflow as tf
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Initialize NLTK components
nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
tokenizer = RegexpTokenizer("[\w']+")

# Retrieve data from MongoDB
documents = collection.find()
paragraphs = []
for doc in documents:
    paragraphs.append(doc['content'])  # Assuming each document has a 'content' field

# Preprocess the data
words = []
classes = []
documents = []

# Create a simple class for each paragraph
for i, paragraph in enumerate(paragraphs):
    tokens = tokenizer.tokenize(paragraph)
    words.extend(tokens)
    documents.append((tokens, f'class_{i}'))  # Assign a class label based on index
    classes.append(f'class_{i}')

# Stem and lower the words
words = [lemmatizer.lemmatize(w.lower()) for w in words]
words = sorted(set(words))
classes = sorted(set(classes))

# Create training data
training_data = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
    
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training_data.append([bag, output_row])

# Shuffle the training data
np.random.shuffle(training_data)
training_data = np.array(training_data)

# Split into input and output
train_x = list(training_data[:, 0])
train_y = list(training_data[:, 1])

# Build the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, input_shape=(len(train_x[0]),), activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(len(train_y[0]), activation='softmax')
])

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)

# Save the model
model.save('chatbot_model.h5')

# Function to predict class
def predict_class(text):
    # Preprocess the input text
    bag = [0] * len(words)
    tokens = tokenizer.tokenize(text)
    tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens]
    
    for w in tokens:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1

    # Predict the class
    prediction = model.predict(np.array([bag]))[0]
    return classes[np.argmax(prediction)]

# Example usage
if __name__ == "__main__":
    user_input = input("You: ")
    response_class = predict_class(user_input)
    print(f"Bot: {response_class}")