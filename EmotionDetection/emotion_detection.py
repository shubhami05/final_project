import requests
import json

def emotion_detector(text_to_analyse):
    if not text_to_analyse.strip():  # Check for blank input
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }, 400  # Return a 400 status code for blank input

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:  # Handle 400 status code
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }, 400

    response = json.loads(response.text)
    emotions = response['emotionPredictions'][0]['emotion']
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    
    dominant_emotion = max(('anger', anger), ('disgust', disgust), ('fear', fear), ('joy', joy), ('sadness', sadness), key=lambda x: x[1])[0]
    answer = {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': dominant_emotion}
    return answer