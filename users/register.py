from application.app import app
from flask import redirect,render_template,request
from users.UserRepository import UserRepository

@app.route("/register",methods = ["POST","GET"])
def register():
    user_repository = UserRepository()
    if request.method == "POST":
        name = request.form['name']
        lname = request.form['lname']
        data_user = user_repository.add_user("aaaaa","asddasas","asdsdasad","asdadsas","asdasdasdas",435453)
        if data_user:
            return redirect(f"/allusers?id={data_user[0][0]}")
    return render_template("register.html",data = "dassdas")