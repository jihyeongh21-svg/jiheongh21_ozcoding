from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@app.route("/")
def index():
    return render_template("sentiment.html")

@sock.route("/ws")
def websocket(ws):
    while True:
        text = ws.receive()
        if text is None:
            break
        
        positives = ["happy", "good", "love", "great"] # 긍정
        negatives = ["fuck", "sad", "bad", "angry"] # 부정

        # for pw in positives:
        #     if pw in text:
        #         sentiment = "긍정 🙂‍"
        if any(pw in text.lower() for pw in positives):
            sentiment = "긍정 🙂‍"

        # for nw in negatives:
        #     if nw in text:
        #         sentiment = "부정 😥"
        elif any(nw in text.lower() for nw in negatives):
            sentiment = "부정 😥"

        else:
            sentiment = "중립 🍀"

        ws.send(sentiment)

if __name__ == "__main__":
    app.run(debug=True)