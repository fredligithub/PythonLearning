from flask import Flask, render_template, request
app = Flask(__name__)

# Default Route and load 'FormTransfer_Student.html' template which has an embedded form
@app.route('/')
def student():
   return render_template('FormTransfer_Student.html')

# After the form in 'FormTransfer_Student.html' is submitted, it will 'POST' request to: 
# http://localhost:9003/result
@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("FormTransfer_Result.html",result = result)

if __name__ == '__main__':
   app.run(host='127.0.0.1',port=9003, debug = True)

# 模板是一个包含响应文本的文件，其中包含用占位变量表示的动态部分，其具体值只在请求的上下文中才能知道。
# 使用真实值替换变量，再返回最终得到的响应字符串，这一过程称为渲染。