from flask import Flask, session, redirect, url_for, escape, request, abort
app = Flask(__name__)
app.secret_key = 'sessiondemohere'

@app.route('/')
def index():
    if 'username' in session:  # Check session exist or not 
        username = session['username'] # If exist, get the value and show on page
        return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"
    else:
        return "You are not logged in <br><a href = '/login'></b>" + "click here to log in</b></a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'].lower() == 'admin':
            session['username'] = request.form['username']
            return redirect(url_for('index')) # url_for()最简单的用法是以函数名作为参数，返回对应的URL。
        else:
            abort(401) # If the login user does not equal to "Admin", will show 401 Unauthenticated error message
    else:
        return  '<form action = "" method = "post">' + \
        '<p><input type = text name = username /></p>' + \
        '<p><input type = submit value = Login /></p>' + \
        '</form>'

#400 − for Bad Request
#401 − for Unauthenticated
#403 − for Forbidden
#404 − for Not Found
#406 − for Not Acceptable
#415 − for Unsupported Media Type
#429 − Too Many Requests

@app.route('/logout', methods =['GET'])
def logout():
    session.pop('username',None)  # Logout, pop up session
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8002, debug = True)