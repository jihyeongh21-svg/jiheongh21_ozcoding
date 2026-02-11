from flask import request, jsonify, Blueprint
from .models import SessionLocal, Todo

todo_bp = Blueprint("todo", __name__)

##########
# CRUD
##########

# READ: 전체 항목 조회
@todo_bp.route("/todos", methods=["GET"])
def get_todos():
    db = SessionLocal()
    todos = db.query(Todo).all()
    db.close()
    return jsonify([{"id": t.id, "task": t.task} for t in todos])


# READ: 특정 항목 조회
@todo_bp.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    db = SessionLocal()
    todo = db.query(Todo).get(todo_id)
    db.close()

    if not todo:
        return jsonify({"error": "해당 할 일이 없습니다"}), 404
    return jsonify({"id": todo.id, "task": todo.task})


# CREATE: 새로운 항목 조회
@todo_bp.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    db = SessionLocal()
    todo = Todo(task=data["task"])
    db.add(todo)
    db.commit()
    db.refresh(todo) # commit 후 자동 생성된 id 불러오기
    db.close()

    return jsonify({"id": todo.id, "task": todo.task}), 201


# UPDATE: 특정 항목 수정
@todo_bp.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    db = SessionLocal()

    todo = db.query(Todo).get(todo_id)
    if not todo:
        db.close()
        return jsonify({"error": "해당 할 일이 없습니다"}), 404

    data = request.get_json()
    todo.task = data["task"]
    db.commit()

    updated = {"id": todo.id, "task": todo.task}
    db.close()
    return jsonify(updated)


# DELETE: 특정 항목 삭제
@todo_bp.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    db = SessionLocal()

    todo = db.query(Todo).get(todo_id)
    if not todo:
        db.close()
        return jsonify({"error": "해당 할 일이 없습니다"}), 404

    db.delete(todo)
    db.commit()
    db.close()
    return jsonify({"deleted": todo_id})