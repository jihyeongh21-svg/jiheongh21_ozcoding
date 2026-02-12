from flask_smorest import Blueprint
from flask import request,jsonify
from flask_jwt_extended import create_access_token
from models import User
from werkzeug.security import check_password_hash,generate_password_hash
from db import db



auth_blp = Blueprint("auth", __name__, description="Authentication",url_prefix="/login")

@auth_blp.route("/",methods=["POST"])
def login():
    if not request.is_json:
        print("if not request.is_json")
        return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400
    
    user = User.query.filter_by(username=username).first()
    print("user come",user)

    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=username)
        print("access_token",access_token)
        return jsonify(access_token=access_token)
    
    else:
        return jsonify({"msg": "Bad username or password"}), 401
    

@auth_blp.route("/register",methods=["POST"])
def register():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username= request.json.get("username", None)
    password= request.json.get("password", None)
    
    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    exist_user = User.query.filter_by(username=username).first()
    if exist_user:
        return jsonify({"msg": "Username already exists"}), 400
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User created successfully"}), 201



