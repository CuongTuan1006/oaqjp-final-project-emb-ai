#URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
#Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
#Input json: { "raw_document": { "text": text_to_analyze } }
import requests, json

def emotion_detector(text):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text }}
    response = requests.post(url, headers = header, json = myobj)
    if response.status_code == 200:
        formatted_response = json(response)
        label = response['label']
        score = response['score']
    else:
        print(response.status_code)
        label = None
        score = None

    return {"label": label, "score": score}

