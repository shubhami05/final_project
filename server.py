from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detection():
   
    text = request.args.get('text')    
    response = emotion_detector(text)

    return f"For the given statement, the system response is 'anger': {0}, 'dispute': {1}, 'fear': {2}, 'joy': {3}, 'sadness': {4}. The dominant emotion is {}."format(response['anger'],response['dispute'],response['fear'],response['joy'],response['sadness'],response['dominant_emotion']) 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)