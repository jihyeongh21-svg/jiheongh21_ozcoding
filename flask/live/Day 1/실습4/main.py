from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello():
    return render_template("hello.html", name="민혁")

@app.route("/user/<username>")
def user(username):
    return render_template("user.html", username=username)

@app.route("/fruits")
def fruits():
    fruits = ["사과", "배", "딸기", "포도"]
    return render_template("fruits.html", fruits=fruits)

if __name__ == "__main__":
    app.run(debug=True)