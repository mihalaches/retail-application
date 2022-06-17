from application.app import app
from libs.token import check_admin_auth
from flask import redirect, render_template, request
from users.UserRepository import UserRepository
from libs.reset_password import reset_password

@app.route("/admin/users",methods=["GET","POST"])
@check_admin_auth
def all_users(user):
    template = "admin_all_users.html"
    user_repo = UserRepository()
    all_users = user_repo.get_all_users()
    if request.method == "POST":
        if "change_first_name" in request.form:
            updated_value = user_repo.update_user("first_name",request.form['change_first_name'],request.form['value'])
            if updated_value:
                return redirect(request.url)
        if "change_last_name" in request.form:
            updated_value = user_repo.update_user("last_name",request.form['change_last_name'],request.form['value'])
            if updated_value:
                return redirect(request.url)
        if "change_rank_user" in request.form:
            updated_value = user_repo.update_user("role",request.form['change_rank_user'],'2')
            if updated_value:
                return redirect(request.url)
        if "change_rank_admin" in request.form:
            updated_value = user_repo.update_user("role",request.form['change_rank_admin'],'1')
            if updated_value:
                return redirect(request.url)
        if "change_country" in request.form:
            updated_value = user_repo.update_user("country",request.form['change_country'],request.form['value'])
            if updated_value:
                return redirect(request.url)
        if "change_phone" in request.form:
            updated_value = user_repo.update_user("phone_number",request.form['change_phone'],request.form['value'])
            if updated_value:
                return redirect(request.url)
        if "change_deposit" in request.form:
            updated_value = user_repo.update_deposit(request.form['change_deposit'],request.form['value'])
            if updated_value:
                return redirect(request.url)
        if "delete_user" in request.form:
            updated_value = user_repo.delete(request.form['delete_user'])
            if updated_value:
                return redirect(request.url)
        if "send_reset_key" in request.form:
            url = request.root_url + "/resetpass"
            reset_password.send_reset_token(request.form['send_reset_key'],url,"token")

    return render_template(template,user=user,all_users = all_users)