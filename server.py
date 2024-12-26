from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/")
def render_home():
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detection():
   
    text = request.args.get('text')    
    response = emotion_detector(text)

    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}, 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}." 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)