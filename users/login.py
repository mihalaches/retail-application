from tkinter.tix import Tree
from application.app import app
from flask import redirect, render_template, request,session, url_for
from libs.token import jwt_token,no_login_req
from users.UserRepository import UserRepository
import bcrypt
from libs.messages import Messages

@app.route("/login",methods=['GET','POST'])
@no_login_req
def login():
    user_repo = UserRepository()
    template = "login.html"
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = user_repo.get_user("email",email)
        if user:
            check_pass = bcrypt.checkpw(password.encode("utf-8"),user.password.encode("utf-8"))
            if check_pass:
                session['token'] = jwt_token.encode(cid=user.cid,email=user.email)
                return redirect(url_for("products_list"))
            return render_template(template,data = {"invalid_password":True,"message":Messages.INVALID_PASSWORD})
        return render_template(template,data = {"invalid_email":True,"message":Messages.INVALID_EMAIL})
    return render_template(template,data ="")