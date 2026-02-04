# jinja2 템플릿 엔지  python에서 만든 데이터를 html에 넣어주는 도구
# render_template()을 통해 삽입
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello')
def home():
    return render_template('hello.html',name = "OZ")
    
if __name__ == '__main__':
    app.run(debug=True,port=5001)  