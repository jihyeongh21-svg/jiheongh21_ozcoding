from flask import Flask

app = Flask(__name__)

@app.route("/") # 127.0.0.1:5000
def home():
    return "홈입니다"

@app.route("/hello") # 127.0.0.1:5000/hello
def hello():
    return "안녕하세요"

@app.route("/user/<name>")
def greet(name):
    return f"{name}님 환영합니다"

if __name__ == '__main__':
    app.run(debug=True)