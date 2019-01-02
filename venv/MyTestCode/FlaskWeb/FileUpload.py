from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

UPLOAD_FOLDER = 'E:/Code/Python/1stPythonEntry/venv/MyTestCode/FlaskWeb/upload/' # File upload folder
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']) # File extension allowed

@app.route('/') # Index file
def upload_file():
    return render_template('FileUpload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        f = request.files['file']
        if f and allowed_file(f.filename):
                filename = secure_filename(f.filename) # secure_filename用来确保文件名是安全的
                f.save(os.path.join(UPLOAD_FOLDER, filename))
                return 'file uploaded to ' + os.path.join(UPLOAD_FOLDER, filename) + ' successfully!'
        else:
                return 'Invalid upload file'

def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8004, debug = True)