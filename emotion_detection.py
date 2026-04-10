# Import the requests library to handle HTTP requests
import requests
import json

# Define a function named emotion_detector that takes a string input
def emotion_detector(text_to_analyse):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create a dictionary with the text to be analyzed
    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': '<name of the dominant emotion>'
    }

    # Set the headers required for the API request
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Send a POST request to the API
    response = requests.post(url, json=myobj, headers=header)

    return response.text 
