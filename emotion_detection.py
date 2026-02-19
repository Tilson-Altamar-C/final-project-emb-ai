import json
import requests

url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_a_analizar):
    # Manejo básico de texto vacío (útil para evitar errores)
    if text_a_analizar is None or str(text_a_analizar).strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    payload = {"raw_document": {"text": text_a_analizar}}
    response = requests.post(url, headers=header, json=payload, timeout=20)

    # Si el servicio responde con error, devolvemos el formato esperado con None
    if response.status_code != 200:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    # Convertimos el response.text en JSON
    response_dict = json.loads(response.text)

    # Extraer emociones del formato típico del servicio
    emotions = response_dict["emotionPredictions"][0]["emotion"]

    scores = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
    }

    #Calculamos la emoción dominante
    dominant = max(scores, key=scores.get)
    scores["dominant_emotion"] = dominant

    return scores
