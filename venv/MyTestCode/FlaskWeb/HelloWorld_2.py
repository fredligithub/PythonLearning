from flask import Flask, render_template
app = Flask(__name__)

# render_template函数的第一个参数是模板的文件名;随后的参数都是键值对,表示模板中变量对应的真实值。

#  {{ ... }} for Expressions to print to the template output
@app.route('/hello/<user>')
def hello_name(user):
   return render_template('HelloUser.html', name = user)

#  {% ... %} for Statements (if..else. this kind of code in html file, etc.)
@app.route('/hello/<int:score>')
def hello_score(score):
   return render_template('HelloScore.html', marks = score)

#  {% ... %} for Statements (if..else. this kind of code in html file, etc.)
@app.route('/hello/list')
def hello_list():
   dict = {'F':50, 'L':60, 'M':70}
   return render_template('HelloList.html', result = dict)

#  {# ... #} for Comments not included in the template output

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=9001, debug = True)