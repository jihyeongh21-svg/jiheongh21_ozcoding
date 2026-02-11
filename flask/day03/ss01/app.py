from flask import Flask, render_template
from flask_mysqldb import MySQL
from flask_smorest import Api
from user_routes import create_user_blueprint

app = Flask(__name__)

# MySQL connection configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'wlgud12'
app.config['MYSQL_DB'] = 'oz'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor' # Optional: return dicts instead of tuples

mysql = MySQL(app)

# OpenApi configuration
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = 'User API'
app.config["API_VERSION"] = 'v1'
app.config["OPENAPI_VERSION"] = '3.0.2'
app.config["OPENAPI_URL_PREFIX"] = '/'
app.config["OPENAPI_SWAGGER_UI_PATH"] = '/swagger-ui'
app.config["OPENAPI_SWAGGER_UI_URL"] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

api = Api(app)
user_blp = create_user_blueprint(mysql)
api.register_blueprint(user_blp)

# HTML interface
@app.route('/user_interface')
def user_interface():
    return render_template('users.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
