"""
Server for Sentiment Analysis Web App.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Render index page.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Run emotion detection on given textToAnalyze request argument.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    if text_to_analyze is None:
        return "No text given to analyze"
    emotions = emotion_detector(text_to_analyze)
    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]
    dominant_emotion = emotions["anger"]
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return f"For the given statement," \
        f"the system response is 'anger': {anger}, " \
        f"'disgust': {disgust}, " \
        f"'fear': {fear}, " \
        f"'joy': {joy} " \
        f"and 'sadness': {sadness}. " \
        f"The dominant emotion is {dominant_emotion}."
