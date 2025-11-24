# AI-Based Emotion Detection Web Application

A **Python Flask web application** that detects emotions in text using IBM Watson Natural Language Understanding (NLU). This repository contains the full code for the backend API, unit tests, and deployment setup.

---

## 🚀 Features

- Detect multiple emotions in any text.
- Identify the dominant emotion.
- Simple REST API for integration.
- Handles invalid inputs gracefully.
- Fully PyLint 10/10 compliant.
- Ready for local or cloud deployment.

---

## ⚡ Installation & Running

```bash


python -m venv venv
source venv/bin/activate       # Linux/macOS
pip install -r requirements.txt

- Run the server
python server.py
- Response Example:
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


- Project Structure

final_project/
├─ EmotionDetection/          # Emotion detection logic using Watson NLP
│   └─ emotion_detection.py
├─ server.py                  # Flask API server
├─ requirements.txt           # Python dependencies
└─ README.md                  # This file

Deployment
	•	Can be deployed locally using Flask.
	•	Can be containerized with Docker for cloud deployment.
