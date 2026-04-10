# Import the requests library to handle HTTP requests
import requests
import json

# Define a function named sentiment_analyzer that takes a string input
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

    # Handle response
#    if response.status_code == 200:
        # Parse the response from the API
#       formatted_response = json.loads(response.text)

        # Extract sentiment label and score
#        label = formatted_response['documentSentiment']['label']
#        score = formatted_response['documentSentiment']['score']

#    elif response.status_code == 500:
#       label = None
#        score = None

#    else:
#        label = None
#        score = None

    # Return the result
#    return {'label': label, 'score': score}