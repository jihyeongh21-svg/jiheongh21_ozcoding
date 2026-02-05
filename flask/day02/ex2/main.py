from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/survey')
def survey():
    questions = [
        '오늘도 열심히 할 자신이 있나요?',
        '이전에 배운 내용은 잘 숙지하고 있나요?',
        '오늘도 열심히 할 자신이 있나요?'
    ]
    return render_template('survey.html',questions = questions)

@app.route('/result',methods=['GET'])
def result():
    answers = request.args.getlist('answer')
    return render_template('result.html',answers=answers)

if __name__ == "__main__":
    app.run(debug=True,port=5001)