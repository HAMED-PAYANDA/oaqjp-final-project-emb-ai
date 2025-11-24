#AI-Based Emotion Detection Web Application

##A Python Flask web application that detects emotions in text using IBM Watson Natural Language Understanding (NLU). This repository contains the full code for the backend API, unit tests, and deployment setup.

⸻

Features
	•	Detects anger, disgust, fear, joy, and sadness in text input.
	•	Returns the dominant emotion.
	•	Flask API for easy integration with other applications.
	•	Error handling for invalid inputs.
	•	Fully PyLint-compliant (10/10).
	•	Ready for web deployment.

Run the server
python server.py

API Usage
	•	Endpoint: /emotionDetector
	•	Method: POST
	•	JSON body:
  {
  "text": "I am feeling very happy today!"
}

	•	Response Example:
  {
  "response": "For the given statement, the system response is 'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.95, 'sadness': 0.05. The dominant emotion is joy.",
  "emotions": {
    "anger": 0.0,
    "disgust": 0.0,
    "fear": 0.0,
    "joy": 0.95,
    "sadness": 0.05,
    "dominant_emotion": "joy"
  }
}


Project Structure

final_project/
├─ EmotionDetection/          # Emotion detection logic using Watson NLP
│   └─ emotion_detection.py
├─ server.py                  # Flask API server
├─ requirements.txt           # Python dependencies
└─ README.md                  # This file

Deployment
	•	Can be deployed locally using Flask.
	•	Can be containerized with Docker for cloud deployment.
