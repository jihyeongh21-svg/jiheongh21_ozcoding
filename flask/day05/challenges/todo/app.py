# app.py
from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy

from db import db
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["JWT_SECRET_KEY"] = "super-secret-key"
app.config["API_TITLE"] = "TOdo API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"

db.init_app(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)
api = Api(app)

# 모델 리소스 불러오기
from models import User, Todo
from routes.todo import todo_blp
from routes.auth import auth_blp

api.register_blueprint(todo_blp)
api.register_blueprint(auth_blp)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True,port= 5001)