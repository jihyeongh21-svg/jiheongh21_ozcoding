from flask import (
    Flask,
    render_template
)
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

user = {
    'admin': 'secret',
    'guest': 'pw123'
}

@auth.verify_password
def verify_password(username, password):
    if username in user and user[username] == password:
        return username

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/protected')
@auth.login_required
def protected():
    return render_template('secret.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)