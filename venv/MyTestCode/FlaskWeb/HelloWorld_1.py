from flask import Flask, request
app = Flask(__name__)

@app.route('/Hello')  # app.route作为路由修饰器
def hello_world():    # hello_world()称之为视图函数。视图函数返回的可以是包含HTML的简单字符串，或者复杂的表单。
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent
    # return 'Hello World!!!'

@app.route('/HelloFred/<name>')  # <name>是路由中的可变（动态）部分；动态部分会被作为参数传给函数。
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/Blog/<int:postID>') # 动态部分可以是int型
def show_blog(postID):
    return 'Blog Number is %d' % postID

@app.route('/Money/<float:salary>')  # 动态部分可以是float型
def show_salary(salary):
    return 'Your salary is %f' % salary

# 默认地址和端口： 127.0.0.1:5000，程序实例通过app.run启动。服务器启动后，会进入轮询，等待并处理请求。
if __name__ == '__main__':
    app.run(debug = True)    