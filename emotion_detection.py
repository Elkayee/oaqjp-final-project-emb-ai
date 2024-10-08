import requests  # Import the requests library to handle HTTP requests
import json
def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    # Extracting sentiment label and score from the response
    emotion_data = formatted_response['emotionPredictions'][0]['emotion']

    # Extracting emotion scores from the response
    disgust = emotion_data['disgust']
    anger = emotion_data['anger']
    fear = emotion_data['fear']
    joy = emotion_data['joy']
    sadness = emotion_data['sadness']
    emotions = {'disgust': disgust, 'anger': anger, 'fear': fear, 'joy': joy, 'sadness': sadness}
    dominant_emotion = max(emotions, key=emotions.get)  # Get the emotion with the highest score
    # Returning a dictionary containing sentiment analysis results
    return {'disgust': disgust, 'anger': anger, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': dominant_emotion}
    