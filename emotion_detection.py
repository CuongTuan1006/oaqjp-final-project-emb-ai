import requests 
#import json

def emotion_detector(text):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text }}
    response = requests.post(url, headers = header, json = myobj)
    return response.text
    """
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    else:
        print(response.status_code)
        label = None
        score = None

    return {"label": label, "score": score}
    """

