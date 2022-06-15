from application.app import app
from flask import redirect, session, url_for
@app.route("/admin/logout")
def logout_admin():
    session.clear()
    return redirect(url_for("login_admin"))