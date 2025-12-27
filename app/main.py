from flask import Flask, render_template, request, redirect, url_for, session, flash
from Logic.auth import check_login

app = Flask(__name__)
app.secret_key = 'ZXCVBNM<>?@123'  # Required to encrypt session cookies

app.config.update(
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=False   # MUST be False for http://127.0.0.1
)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/success')
def success():
    # return render_template('success.html')
    if 'username' in session:
        return render_template('success.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove user from session
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_login(username, password):
            session['username'] = username
            return redirect(url_for('success'))
        else:
            message = 'Invalid username or password'
    return render_template('login.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
