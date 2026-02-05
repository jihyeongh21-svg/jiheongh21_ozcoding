from flask import Flask,jsonify,request
from flasgger import Swagger


app = Flask(__name__)

swagger = Swagger(app)

# 임시 저장소
todos = {
    1:'학습',
    2:'운동'
}

# Read: 전체 항목 조회
@app.route('/todos',methods = ['GET'])
def get_todos():
    return jsonify(todos)

# Read: 특정 항목 조회
@app.route('/todos/<int:todo_id>',methods = ['GET'])
def get_todo(todo_id):
    task  = todos.get(todo_id)
    if not task:
        return jsonify({'error':'not found'}), 404
    else:
        return jsonify({todo_id:task})

# Create: 항목 추가

@app.route('/todos',methods = ['POST'])
def add_todo():
    data =  request.get_json()
    new_id  = max(todos.keys()) + 1 if todos else 1
    todos[new_id] = data.get('task')
    return jsonify({new_id:todos[new_id]}), 201

# Update: 항목 수정
@app.route('/todos/<int:todo_id>',methods = ['PUT'])
def update_todo(todo_id):
    if todo_id not in todos:
        return jsonify({'error':'not found'}), 404
    data = request.get_json()
    todos[todo_id] = data.get('task')
    return jsonify({todo_id:todos[todo_id]})

# Delete: 항목 삭제

@app.route('/todos/<int:todo_id>',methods = ['DELETE'])
def delete_todo(todo_id):
    task = todos.get(todo_id)
    if todo_id not in todos:
        return jsonify({'error':'not found'}), 404
    else:
        deleted = todos.pop(todo_id)
        return jsonify({"deleted": deleted}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)
