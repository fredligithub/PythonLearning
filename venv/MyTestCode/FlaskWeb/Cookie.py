from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Cookie_Index.html")

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
       user = request.form['nm']
   
   resp = make_response(render_template('Cookie_ReadCookie.html'))
   resp.set_cookie('userID', user)
   
   return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>Welcome '+name+'</h1>'

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8001, debug = True)