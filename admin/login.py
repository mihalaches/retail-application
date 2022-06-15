from email import message
from application.app import app
from flask import redirect, render_template, request,session, url_for
from libs.token import jwt_token,no_login_req_admin
from users.UserRepository import UserRepository
import bcrypt
from libs.messages import Messages

@app.route("/admin/login",methods=['GET','POST'])
@no_login_req_admin
def login_admin():
    user_repo = UserRepository()
    template = "login_admin.html"
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = user_repo.get_user("email",email)
        if user:
            if user.role == "ADMIN":
                check_pass = bcrypt.checkpw(password.encode("utf-8"),user.password.encode("utf-8"))
                if check_pass:
                    session['token'] = jwt_token.encode(cid=user.cid,email=user.email)
                    return redirect(url_for("view_orders"))
                return render_template(template,data = {"invalid_password":True,"message":Messages.INVALID_PASSWORD})
            print("NO ADMIN")
            return render_template(template,data = {"no_admin":True, "message":Messages.NO_ADMIN_ACCOUT})
        return render_template(template,data = {"invalid_email":True,"message":Messages.INVALID_EMAIL})
    return render_template(template,data ="")