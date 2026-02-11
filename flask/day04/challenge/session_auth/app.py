from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    flash
    )
from datetime import timedelta


# from datetime import timedelta
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 예: 7일
app =Flask(__name__)
app.secret_key = 'flask-secret-key' # .env또는 yaml에 저장 
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)


# admin
users = {
    'admin': 'pw123',
    'admin2': 'pw456'
}

@app.route('/')
def  index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        session['username'] = username
        session.permanent = True
        return redirect('/secret')
    else:
        flash('Invalid username or password')
        return redirect('/')

@app.route('/secret')
def secret():
    if 'username' in session:
        return render_template('secret.html')
    else:
        return redirect('/')

# 로그아웃
@app.route('/logout')
def logout():
    session.pop('username', None)
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True,port=5001)