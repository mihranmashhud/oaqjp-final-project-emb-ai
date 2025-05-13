import requests
import json

def emotion_detector(text_to_analyze: str):
    resp = requests.get(
        "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict",
        headers={
            "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        },
        json={"raw_document": {"text": text_to_analyze}},
    )

    json_resp = json.loads(resp.text)

    return json_resp
