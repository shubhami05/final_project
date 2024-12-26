"""
server.py

This module implements a Flask web application that detects emotions
from user-provided text input. It uses the emotion_detector function
from the EmotionDetection module to analyze the text and return
emotion predictions.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_home() -> str:
    """Render the home page."""
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detection() -> str:
    """Detect emotions from the provided text."""
    text = request.args.get('text')

    if not text:
        response = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return response, 400
    response, status_code = emotion_detector(text)
    if status_code == 400 or response['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. The dominant emotion is "
        f"{response['dominant_emotion']}."
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
