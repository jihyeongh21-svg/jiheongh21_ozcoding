from flask import Flask,request,jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base,sessionmaker
import os

app = Flask(__name__)


##################
# DB설정
##################
BASE_DIR=os.path.dirname(__file__)
INSTANCE_DIR=os.path.join(BASE_DIR,'instance')
os.makedirs(INSTANCE_DIR,exist_ok=True)#exist_ok 폴더 존재할 경우에 pass
DATABASE_URL = f"sqlite:///{os.path.join(INSTANCE_DIR,'todos.db')}"

engine = create_engine(DATABASE_URL,echo=True)

# engine = create_engine('sqlite:///instance/todos.db',echo=True)
Sessionlocal = sessionmaker(bind=engine)

##################
# 모델 정의
##################

Base = declarative_base()
Base.metadata.create_all(bind=engine)
# 테이블 생섳

class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, nullable=False)
    
    def __repr__(self):
        return f"Todo(id={self.id}, task={self.task})"
    
Base.metadata.create_all(bind=engine)


##########
# CRUD
##########

# Read: 전체 항목 조회
@app.route('/todos',methods = ['GET'])
def get_todos():
    db = Sessionlocal()
    todos = db.query(Todo).all()
    db.close
    return jsonify([{"id":todo.id,"task":todo.task} for todo in todos])


# Read: 특정 항목 조회
@app.route('/todos/<int:todo_id>',methods = ['GET'])
def get_todo(todo_id):
    db = Sessionlocal()
    todo  = db.query(Todo).get(todo_id)
    db.close()
    if not todo:
        return jsonify({'error':'not found'}), 404
    else:
        return jsonify({todo_id:todo.task}),201

# Create: 항목 추가

@app.route('/todos',methods = ['POST'])
def add_todo():
    data =  request.get_json()
    db = Sessionlocal()
    todo = Todo(task = data['task'])
    db.add(todo)
    db.commit()
    db.refresh(todo)
    # 데이터 베이스 갱신
    db.close()
    return jsonify({"id":todo.id,'task':todo.task}), 201

# Update: 항목 수정
@app.route('/todos/<int:todo_id>',methods = ['PUT'])
def update_todo(todo_id):
    db = Sessionlocal()
    todo = db.query(Todo).get(todo_id)
    if not todo:
        db.close()
        return jsonify({'error':'not found'}), 404
    data = request.get_json()
    todo.task = data['task']
    db.commit()
    # 왜 리프레쉬 안하고 따로 저장?
    update_todo = {"id":todo.id,"task":todo.task}
    db.close()
    return jsonify(update_todo), 200

# Delete: 항목 삭제

@app.route('/todos/<int:todo_id>',methods = ['DELETE'])
def delete_todo(todo_id):
    db = Sessionlocal()
    todo = db.query(Todo).get(todo_id)
    if not todo:
        db.close()
        return jsonify({'error':'not found'}), 404
    db.delete(todo)
    db.commit()
    db.close()
    return jsonify({"deleted":todo_id}),201


if __name__ == '__main__':
    app.run(debug=True, port=5001)