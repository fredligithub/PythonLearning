from flask import Flask, render_template
app = Flask(__name__)

# 调用项目templates文件夹下的"index.html"文件. 
# 在"index.html"文件中, 又会引用"static"文件夹下的hello.js文件

# 默认设置下，Flask在程序根目录中名为static的子目录中寻找静态文件。
@app.route("/")
def index():
   return render_template("index.html")

if __name__ == '__main__':
   app.run(host='127.0.0.1',port=9002, debug = True)