from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields
from db import db
from models.user import User

# 1. 스키마 정의 (데이터의 모양을 정의)
class UserSchema(Schema):
    id = fields.Int(dump_only=True)   # 출력할 때만 사용 (서버가 생성하므로)
    name = fields.Str(required=True)  # 필수 입력
    email = fields.Str(required=True) # 필수 입력

user_blp = Blueprint('Users', 'users', description='Operations on users', url_prefix='/users')

@user_blp.route('/')
class UserList(MethodView):
    # 전체 조회
    # List many=True 
    @user_blp.response(200, UserSchema(many=True))
    def get(self):
        #jsonify()없이  DB 객체 리스트를 그대로 리턴
        # 스키마가 알아서 JSON으로 변환
        return User.query.all()

    # 생성
    @user_blp.arguments(UserSchema) # 입력 데이터 검증 (자동으로 request.json을 읽음)
    @user_blp.response(201, UserSchema) # 생성된 객체를 반환하면 JSON으로 변환
    def post(self, new_data):
        print('요청')
        new_user = User(name=new_data['name'], email=new_data['email'])
        
        db.session.add(new_user)
        db.session.commit()
        
        return new_user

@user_blp.route('/<int:user_id>')
class Users(MethodView):
    # id 조회
    @user_blp.response(200, UserSchema)
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user

    #  수정
    @user_blp.arguments(UserSchema) # 수정할 데이터를 받음
    @user_blp.response(200, UserSchema) # 수정된 결과 반환
    def put(self, update_data, user_id):
        user = User.query.get_or_404(user_id)
        
        user.name = update_data['name']
        user.email = update_data['email']

        db.session.commit()
        return user

    #  삭제
    @user_blp.response(204) # 204 No Content는 본문이 없음
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        # return 값 없음