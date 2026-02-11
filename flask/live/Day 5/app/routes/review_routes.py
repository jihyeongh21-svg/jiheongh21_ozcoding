"""
라우트 (Controller Layer)
- 사용자가 요청한 URL을 처리하고
- 서비스 계층을 호출해서 DB 조작
- 결과를 템플릿에 전달
"""

from flask import Blueprint, render_template, request, redirect, url_for
from app.services.review_service import (
    # TODO: get_all_reviews, create_review, get_review_by_id,
    #       update_review, delete_review 함수를 불러오세요
)

# 블루프린트 생성
review_bp = Blueprint("review", __name__)

@review_bp.route("/")
def index():
    """리뷰 목록 + 평균 별점"""
    # TODO: 리뷰 목록을 가져오세요 (service의 get_all_reviews)
    # TODO: 평균 별점을 계산하세요 (리뷰가 있으면 rating 평균, 없으면 0)
    # TODO: index.html 템플릿에 reviews, avg_rating을 전달해서 렌더링하세요
    pass


@review_bp.route("/new", methods=["GET", "POST"])
def new_review():
    """새 리뷰 작성"""
    # TODO: request.method 가 POST 인지 확인하세요
    # TODO: form 데이터(title, content, rating)를 받아오세요
    # TODO: service의 create_review 함수를 호출해서 DB에 저장하세요
    # TODO: 저장 후 index 페이지로 redirect 하세요
    # TODO: GET 요청일 경우 new.html 템플릿을 렌더링하세요
    pass


@review_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_review(id):
    """리뷰 수정"""
    # TODO: service의 get_review_by_id 함수로 해당 id의 리뷰를 가져오세요
    # TODO: POST 요청일 경우 수정된 데이터(title, content, rating)를 받아서 service의 update_review 실행
    # TODO: 수정 후 index 페이지로 redirect 하세요
    # TODO: GET 요청일 경우 edit.html 템플릿을 렌더링하세요 (review 전달)
    pass


@review_bp.route("/delete/<int:id>")
def delete_review_route(id):
    """리뷰 삭제"""
    # TODO: service의 delete_review 함수를 실행해서 해당 리뷰를 삭제하세요
    # TODO: 삭제 후 index 페이지로 redirect 하세요
    pass