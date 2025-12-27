from flask import Flask, render_template, request, redirect, url_for, session, flash
from Logic import common

import os

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
# print("--FLASK_SECRET_KEY---",os.getenv("FLASK_SECRET_KEY"))

app.secret_key = os.getenv("FLASK_SECRET_KEY")

app.config.update(
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=False   
)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove user from session
    return redirect(url_for('login'))




@app.route('/user/dashboard')
def user_success():
    if 'username' in session:
        stock_data=common.get_stock_data()
        return render_template('user_dashboard.html', username=session['username'],stock=stock_data)
    else:
        # return redirect(url_for('login'))
        return render_template("login.html")


@app.route('/agent/dashboard')
def admin_dashboard():    
    if 'username' in session:
        if session.get('login_type') != 'agent':
            message = 'Unauthorize Access to Admin portal'
            session.pop('username', None)
            session.pop('login_type', None)
            return render_template('login.html', message=message)
        else:
            return render_template('admin_dashboard.html', username=session['username'])
    else:
        # return redirect(url_for('login'))
        return render_template("login.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        login_type = request.form['login_type']
        user = common.check_login(username, password, login_type)

        if user and user["email"] and user["type"]:
            session['username'] = user["name"]
            session['login_type'] = user["type"]
            if login_type == "agent":
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('user_success'))
        else:
            message = 'Invalid username or password'
    return render_template('login.html', message=message)

# @app.route('/admin_dashboard')
# def admin_dashboard():
#     username = session['username']
#     return render_template('admin_dashboard.html', username=username)

# @app.route('/manage_users')
# def manage_users():
#     # Handle user management
#     pass

# @app.route('/manage_stock')
# def manage_stock():
#     # Handle stock management
#     pass

if __name__ == '__main__':
    app.run(debug=True)

