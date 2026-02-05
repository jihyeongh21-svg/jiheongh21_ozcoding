from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/user/<name>')
def user(name):
    return jsonify(message= f"Hello {name}")
    # return {"message": f"Hello {name}"}

if __name__ == '__main__':
    app.run(debug=True, port=5001)