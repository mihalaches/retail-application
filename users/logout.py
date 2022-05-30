from application.app import app
from flask import redirect,session,url_for

@app.route("/logout",methods=["GET"])
def logout():
    session.clear()
    return redirect(url_for('login'))