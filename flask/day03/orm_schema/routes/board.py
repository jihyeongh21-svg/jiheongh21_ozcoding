from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields
from db import db
from models.board import Board

# 1. Board 스키마 정의
class BoardSchema(Schema):
    id = fields.Int(dump_only=True) # 출력 전용 (DB가 생성)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    
    # [핵심 포인트 1] 입력(Load) 할 때만 필요한 필드
    # 게시글을 쓸 때는 user_id를 받아야 하지만, 보여줄 때는 author_name을 보여줄 거라 숨김
    user_id = fields.Int(required=True, load_only=True)
    
    # [핵심 포인트 2] 출력(Dump) 할 때만 필요한 필드
    # attribute="author.name"을 쓰면 board.author.name 값을 자동으로 가져옵니다!
    author_name = fields.Str(dump_only=True, attribute="author.name")

board_blp = Blueprint('Boards', 'boards', description='Operations on boards', url_prefix='/board')

@board_blp.route('/')
class BoardList(MethodView):
    # [GET] 전체 조회
    @board_blp.response(200, BoardSchema(many=True))
    def get(self):
        # 이제 리스트 컴프리헨션([...]) 필요 없음! 객체 리스트를 그냥 던지면 됨
        return Board.query.all()

    # [POST] 게시글 작성
    @board_blp.arguments(BoardSchema)
    @board_blp.response(201, BoardSchema)
    def post(self, board_data):
        # board_data는 이미 검증된 딕셔너리: {'title': '...', 'content': '...', 'user_id': 1}
        
        # **board_data로 한방에 넣을 수 있음
        new_board = Board(**board_data)
        
        db.session.add(new_board)
        db.session.commit()
        
        return new_board

@board_blp.route('/<int:board_id>')
class BoardResource(MethodView):
    # [GET] 단건 조회
    @board_blp.response(200, BoardSchema)
    def get(self, board_id):
        board = Board.query.get_or_404(board_id)
        return board

    # [PUT] 수정
    @board_blp.arguments(BoardSchema)
    @board_blp.response(200, BoardSchema)
    def put(self, board_data, board_id):
        board = Board.query.get_or_404(board_id)
        
        board.title = board_data['title']
        board.content = board_data['content']
        # user_id는 수정하지 않음 (작성자를 바꾸진 않으니까요)

        db.session.commit()
        return board

    # [DELETE] 삭제
    @board_blp.response(204)
    def delete(self, board_id):
        board = Board.query.get_or_404(board_id)
        db.session.delete(board)
        db.session.commit()