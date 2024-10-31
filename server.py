"""FInal project: Emotion Detection"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route("/")
def render_index_page():
    """Renders home page"""
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detect():
    """Analyses text emotions"""
    text = request.args.get('textToAnalyze')
    emotions = emotion_detector(text)

    if emotions['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    result = ("For the given statement, the system response is "
    f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}"
    f", 'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. "
    f"The dominant emotion is {emotions['dominant_emotion']}.")

    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
