import requests
import json

def emotion_detector(text_to_analyze):
    """Detect emotions in a text"""
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json= { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL,json=input_json,headers=headers)
    if response.status_code==200:
        formatted_response = json.loads(response.text)

        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }

        dom_emotion = max(emotions,key=lambda k: emotions[k])
        emotions['dominant_emotion'] = dom_emotion
        
        
    elif response.status_code == 400:
        emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        

    return emotions