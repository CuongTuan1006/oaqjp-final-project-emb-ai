"""
Define Emotion Detection web app
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detect():
    """
    Get emotion prediction
    """
    text = request.args.get('textToAnalyze')
    emo = emotion_detector(text)
    if emo['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    items = [f"'{k}': {v}" for k, v in emo.items() if k != 'dominant_emotion']
    formatted_emotions = f"{', '.join(items[:-1])} and {items[-1]}"
    str_rt = f"For the given statement, the system response is {formatted_emotions}"
    str_rt += f"The dominant emotion is {emo['dominant_emotion']}"
    return str_rt

@app.route('/')
def render_page():
    """
    Render interface
    """
    return render_template('index.html')

if __name__ == "main":
    # Run server
    app.run(host = "0.0.0.0", port = 5000)
