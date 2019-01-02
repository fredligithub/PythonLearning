from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/login')
def index():
    return render_template('login.html')

@app.route('/loginsubmit')
def success():
    if request.method == 'POST':
        email = request.form['email']
        return render_template('success.html', email = email)
    else:
        pass
        
if __name__ == '__main__':
    app.run(debug=True)