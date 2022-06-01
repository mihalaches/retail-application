from application.app import app
from flask import render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os
from libs.token import check_auth



UPLOAD_FOLDER = 'application\static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/test", methods = ["POST","GET"])
@check_auth
def test(user):
    if request.method == 'POST':
        print(request.files)
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('test', name=filename))
    return render_template("test.html",user = user.serialize())