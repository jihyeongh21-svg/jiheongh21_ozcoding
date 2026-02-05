from flask import Flask, jsonify
from flasgger import Swagger


app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def hello():
    return jsonify(massage = 'asd')
if __name__ == '__main__':
    app.run(debug=True, port=5001)