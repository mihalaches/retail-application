from application.app import app
from flask import render_template, request
from libs.token import check_auth, jwt_token
from libs.reset_password import reset_password
from users.UserRepository import UserRepository

@app.route("/resetpass",methods=["GET",'POST'])
def resetpass():
    user_repo = UserRepository()
    template = "reset_pass.html"
    path_param_to_search = "token"
    url = request.url
    token = request.args.get(path_param_to_search)
    if token:
        try:
            decoded_token = jwt_token.decode(token)
        except:
            return render_template(template,data = {"data_reset":"Invalid token","set_pass_page":False})
        if jwt_token.check_valability(token):
            if user_repo.get_user("cid",decoded_token.get("cid")):
                if request.method == "POST":
                    password = request.form['password']
                    cpassword = request.form['cpassword']
                    if password != cpassword:
                        return render_template(template,data={"set_pass_page":True,"data_reset":"Confirm password must match password!"})
                    data_updated = user_repo.update_password(decoded_token['cid'],password)
                    if data_updated:
                        return render_template(template,data = {"data_reset":"Password updated!","set_pass_page":False})
                return render_template(template,data={"set_pass_page":True})
        else:
            return render_template(template,data = {"data_reset":"Invalid token","set_pass_page":False})
    if request.method == "POST":
        email = request.form['email']
        data_reset = reset_password.send_reset_token(email,url,path_param_to_search)
        return render_template(template,data = {"data_reset" : data_reset,"set_pass_page":False})

    return render_template(template,data = {"data_reset":None,"set_pass_page":False})