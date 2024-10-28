"""That application runs an emotion detector."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
# Instantiate Flask functionality
app = Flask("EmotionDetector")

@app.route('/emotionDetector')
def response():
    """Response function"""
    text_to_analyze = request.args.get('textToAnalyze')
    emotion_dict = emotion_detector(text_to_analyze)
    dominant_emotion = emotion_dict['dominant_emotion']
    emotion_dict.pop('dominant_emotion')

    if dominant_emotion is None:
        return "Invalid text! Please try again!."
    return f"For the given statement, the system response is {emotion_dict}. \
    The dominant emotion is {dominant_emotion}"

@app.route("/")
def render_index_page():
    """function runs on load of page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5007)
