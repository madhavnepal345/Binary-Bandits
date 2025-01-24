import os 
from google.cloud import aiplatform

PROJECT_ID='midyear-arcade-448818-s8'
LOCATION="asia-south1"


aiplatform.init(project=PROJECT_ID,location=LOCATION)


MODEL_NAME="text-bison"


def chat_with_model():
    model=aiplatform.gapic.PrdictionServiceClient()
    endpoint=aiplatform.Endpoint(MODEL_NAME)

    response=endpoint.predict(instance=[{"content":prompt}])

    return response.predictions[0]['content']

if __name__=="__main__":
    print("Welcome the Brainy Bot !!! Type 'exit to quite")


    while True:
        prompt=input("Ask me anything ")
        if prompt.lower()=='exit':
            break
        response=chat_with_model(prompt)
        print("Response:" ,response)


