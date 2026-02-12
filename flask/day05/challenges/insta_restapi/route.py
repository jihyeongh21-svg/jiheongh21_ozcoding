# routes.py
from flask import Blueprint, request, jsonify, render_template
# models.py에서 만든 함수들을 다 가져옵니다.
from model import users, add_user, add_post_to_user, get_user_posts, like_user_post, delete_user, get_all_users

user_bp = Blueprint('user_bp', __name__)

# 메인 페이지 (HTML)
@user_bp.route('/')
def index():
    return render_template('index.html')

# 1. 사용자 조회 및 생성
@user_bp.route("/users", methods=["GET", "POST"])
def users_route():
    if request.method == "GET":
        return get_all_users() 
    
    elif request.method == "POST":
        request_data = request.get_json()
        return add_user(request_data) 

# 2. 게시물 추가
@user_bp.route("/users/post/<string:username>", methods=["POST"])
def add_post_route(username):
    request_data = request.get_json()
    return add_post_to_user(username, request_data)

# 3. 사용자별 게시물 조회
@user_bp.route("/users/post/<string:username>", methods=["GET"])
def get_posts_route(username):
    return get_user_posts(username)

# 4. 좋아요 증가
@user_bp.route("/users/post/like/<string:username>/<string:title>", methods=["PUT"])
def like_post_route(username, title):
    return like_user_post(username, title)

# 5. 사용자 삭제
@user_bp.route("/users/<string:username>", methods=["DELETE"])
def delete_user_route(username):
    return delete_user(username)