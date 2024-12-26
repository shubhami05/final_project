from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_home():
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detection():
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
    
    try:
        response, status_code = emotion_detector(text)  
        
        if status_code == 400 or response['dominant_emotion'] is None:
            return "Invalid text! Please try again!", 400
        
        return (f"For the given statement, the system response is "
                f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
                f"'fear': {response['fear']}, 'joy': {response['joy']}, "
                f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}.")

    except Exception as e:
        return f"{str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)