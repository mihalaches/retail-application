from email import message
from application.app import app
from flask import redirect,render_template,request
from users.UserRepository import UserRepository
from libs.messages import Messages

@app.route("/register",methods = ["POST","GET"])
def register():
    template = "register.html"
    user_repository = UserRepository()
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            return render_template(template, data = {"pass_match" : False,"message" : Messages.PASSWORD_NOT_MATCH_WITH_CONFIRM})
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        country = request.form['country']
        data_user = user_repository.add_user(email,first_name,last_name,password,country,phone_number)
        if data_user:
            return render_template(template, data = {"pass_match" : True, "message" : Messages.SUCCESS_REGISTER , "user_found" : True})
        else:
            return render_template(template, data = {"pass_match" : True, "message" : Messages.DUPLICATE_EMAIL , "duplicate_email" : False})
    return render_template(template, data = {"pass_match" : True})