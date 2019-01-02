from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.163.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'fred82li@163.com'
app.config['MAIL_PASSWORD'] = '' # Password Here
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True # 在163邮箱设置里面可以看到此项设置
mail = Mail(app)

@app.route("/")
def index():
    msg = Message("Hello", sender="fred82li@163.com",recipients=["fred1982li@163.com"])
    msg.body = "testing"
    mail.send(msg)
    return "Mail is sent..."

if __name__ == '__main__':
   app.run(host='127.0.0.1',port=8005, debug = True)