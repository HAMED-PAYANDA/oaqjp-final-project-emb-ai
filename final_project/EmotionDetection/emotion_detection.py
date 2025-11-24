# final_project/emotion_detection.py
"""
emotion_detector(text_to_analyze) -> returns the 'text' attribute from the EmotionPredict response.

Usage:
    from final_project.emotion_detection import emotion_detector
    print(emotion_detector("I love this new technology."))
"""

import requests
from typing import Any, Optional

WATSON_EMOTION_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
    "Content-Type": "application/json",
}


def _find_text_attribute(obj: Any) -> Optional[str]:
    """
    Search the response JSON recursively for a 'text' attribute and return
    the first string value found. Returns None if no such attribute exists.
    """
    if isinstance(obj, dict):
        # check keys in this dict first
        if "text" in obj and isinstance(obj["text"], str):
            return obj["text"]
        for v in obj.values():
            found = _find_text_attribute(v)
            if found is not None:
                return found
    elif isinstance(obj, list):
        for item in obj:
            found = _find_text_attribute(item)
            if found is not None:
                return found
    return None


def emotion_detector(text_to_analyze: str, timeout: float = 10.0) -> dict:
    """
    Sends text_to_analyze to Watson EmotionPredict and returns
    a dictionary with emotion scores and dominant emotion.

    If text_to_analyze is blank or the server returns status_code 400,
    returns all keys with None values.
    """

    import json
    import requests

    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(WATSON_EMOTION_URL, headers=HEADERS, json=payload, timeout=timeout)
    except requests.RequestException as e:
        raise RuntimeError(f"Request failed: {e}") from e

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    try:
        resp_json = response.json()
    except ValueError as e:
        raise RuntimeError("Response was not valid JSON") from e

    # Extract emotion scores as before
    try:
        emotions = resp_json["emotionPredictions"][0]["emotion"]
    except Exception as e:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    anger = emotions.get("anger", 0)
    disgust = emotions.get("disgust", 0)
    fear = emotions.get("fear", 0)
    joy = emotions.get("joy", 0)
    sadness = emotions.get("sadness", 0)

    emotion_scores = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {**emotion_scores, "dominant_emotion": dominant_emotion}
    