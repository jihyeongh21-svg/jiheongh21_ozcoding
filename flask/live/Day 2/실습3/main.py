from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/user/<name>')
def user(name):
    return jsonify(message=f"{name}, BE캠프에 오신 걸 환영합니다")
    # return {"message": f"{name}, BE캠프에 오신 걸 환영합니다"}

if __name__ == "__main__":
    app.run(debug=True)