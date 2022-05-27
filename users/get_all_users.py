from application.app import app
from users.UserRepository import UserRepository
from flask import jsonify, request, session

@app.route("/allusers",methods = ["POST","GET"])
def get_all_users():
    session['test'] = "testvalue"
    print(session)
    user_repository = UserRepository()
    all_users = user_repository.get_all_users()
    if request.args.get("id"):
        specific_user = user_repository.get_user_by_id(request.args.get("id"))
        return jsonify([{"id":specific_user[0],"name" : specific_user[1], "last_name" : specific_user[2]}])
    return jsonify([{"id":obj_data[0],"name" : obj_data[1], "last_name" : obj_data[2]} for obj_data in all_users])