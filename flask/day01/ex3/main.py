# jinja2 템플릿 엔지  python에서 만든 데이터를 html에 넣어주는 도구
# render_template()을 통해 삽입
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello')
def home():
    return render_template('hello.html',name = "OZ")

@app.route('/user/<username>')
def user(username):
    return render_template('user.html',username = username)

@app.route('/fruits')
def fruits():
    fruits = ["사과",'바나나','오렌지','포도','딸기']
    return render_template('fruits.html',fruits = fruits)

if __name__ == '__main__':
    app.run(debug=True,port=5001)  