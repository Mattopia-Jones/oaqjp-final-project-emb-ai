import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create a dictionary with the text to be analyzed
    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    # Set the headers required for the API request
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Send a POST request to the API
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response
    if response.status_code == 200:
        response_dict = response.json()
        # Extract emotion scores from the response
        emotions = response_dict.get('emotionPredictions', [{}])[0].get('emotion', {})
        
        # Find dominant emotion
        dominant_emotion = max(emotions, key=emotions.get) if emotions else None
        
        # Return structured dictionary
        return {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0),
            'dominant_emotion': dominant_emotion      
        }
    else:
        # Handle error response
        return {
            'error': 'API request failed',
            'status_code': response.status_code
        }
        
