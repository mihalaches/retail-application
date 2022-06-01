from application.app import app 
from libs.token import check_auth
from flask import render_template, request

@app.route("/products", methods = ["GET","POST"])
@check_auth
def products_list(user):
    if request.method == "POST":
        print(request.form)
    return render_template("products_list.html",user = user.serialize())