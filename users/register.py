from application.app import app
from flask import redirect,render_template,request
from users.UserRepository import UserRepository

@app.route("/register",methods = ["POST","GET"])
def register():
    user_repository = UserRepository()
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        country = request.form['country']
        data_user = user_repository.add_user(email,first_name,last_name,password,country,phone_number)
        if data_user:
            return redirect(f"/allusers?id={data_user['cid']}")
    return render_template("register.html",data = "dassdas")