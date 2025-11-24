"""
server.py

This module defines a Flask-based web server for emotion detection
using the EmotionDetection library. It handles routes, request validation,
response formatting, and error handling.
"""

from flask import Flask, request, jsonify
# pylint: disable=import-error
from EmotionDetection.emotion_detection import emotion_detector

# Initialize Flask application
app = Flask(__name__)


def format_emotion_response(result):
    """
    Format the emotion detection results into a readable string.

    Args:
        result (dict): Emotion detection result containing
                       'anger', 'disgust', 'fear', 'joy',
                       'sadness', and 'dominant_emotion'.

    Returns:
        str: Formatted response string.
    """
    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


@app.route('/emotionDetector', methods=['POST'])
def detect_emotion_route():
    """
    Flask route to detect the emotion of a given text.

    Expects a POST request with JSON payload:
    {
        "text": "Your input text here"
    }

    Returns:
        Response: JSON response containing formatted emotion data or error message.
    """
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    text_to_analyze = data["text"]
    result = emotion_detector(text_to_analyze)

    # Handle blank input or invalid result
    if not result or result.get("dominant_emotion") is None:
        return jsonify({"response": "Invalid text! Please try again!"}), 400

    formatted_response = format_emotion_response(result)
    return jsonify({"response": formatted_response, "emotions": result})


@app.errorhandler(404)
def handle_404_error():  # Removed unused argument
    """
    Custom handler for 404 Not Found errors.

    Returns:
        Response: JSON response with error message and 404 status code.
    """
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def handle_500_error():  # Removed unused argument
    """
    Custom handler for 500 Internal Server errors.

    Returns:
        Response: JSON response with error message and 500 status code.
    """
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)