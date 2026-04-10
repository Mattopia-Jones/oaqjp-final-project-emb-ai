"""
Adding this docstring for validation.
"""
# Import Flask, render_template, request
from flask import Flask, render_template, request

# Import the sentiment_analyzer function from the package created
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")

def emote_detector():

@app.route("/emotionDetector")

def emote_detector():
    """
    Retrieve text from request and perform emotion detection
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the response is None or invalid
    if response is None or response.get('dominant_emotion') is None:
        return "Invalid text! Please try again."
    
    # Extract emotions from response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Return a formatted string with all emotion scores
    return f"Text identified with emotions: Anger: {anger_score}, Disgust: {disgust_score}, Fear: {fear_score}, Joy: {joy_score}, Sadness: {sadness_score}. Dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
