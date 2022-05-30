from application.app import app
from flask import render_template,session
from libs.token import jwt_token

@app.route("/login",methods=['GET'])
def login():
    session['token'] = jwt_token.encode(cid = 1, email = "mihalachesebi06@gmail.com")
    return render_template("login.html")