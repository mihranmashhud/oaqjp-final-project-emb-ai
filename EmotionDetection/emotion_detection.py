import requests
import json

def emotion_detector(text_to_analyze: str):
    resp = requests.post(
        "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict",
        headers={
            "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        },
        json={"raw_document": {"text": text_to_analyze}},
    )
    if resp.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    json_resp = json.loads(resp.text)

    emotions = json_resp["emotionPredictions"][0]["emotion"]

    dominant_emotion_score = 0
    dominant_emotion = ""
    for emotion, score in emotions.items():
        if score > dominant_emotion_score:
            dominant_emotion_score = score
            dominant_emotion = emotion

    emotions["dominant_emotion"] = dominant_emotion
    return emotions


