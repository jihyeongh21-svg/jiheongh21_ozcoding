from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

# user
users = [
    {'username': 'test1' , 'name':'abc1'},
    {'username': 'test2' , 'name':'abc2'},
    {'username': 'test3' , 'name':'abc3'}
]

@app.route('/')
def index():    
    return render_template('index.html',users=users)

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        users.append({'username':username,'name':name})
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<username>',methods=['POST','GET'])
def edit(username):
    user = next((user for user in users if user['username'] == username),None)
    if not user:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        user['name'] = request.form['name']
        return redirect(url_for('index'))
    
    return render_template('edit.html',user=user)

@app.route('/delete/<username>')
def delete(username):
    global users
    users = [user for user in users if user['username'] != username]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True,port=5001)
                    