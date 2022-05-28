from application.app import app
from users.UserRepository import UserRepository
from flask import jsonify, request, session

@app.route("/allusers",methods = ["POST","GET"])
def get_all_users():
    session['test'] = "testvalue"
    print(session)
    user_repository = UserRepository()
    all_users = user_repository.get_all_users()
    print(all_users)
    if request.args.get("id"):
        specific_user = user_repository.get_user_by_id(request.args.get("id"))
        return jsonify([{"id":specific_user['cid'],"name" : specific_user['first_name'], "last_name" : specific_user['last_name']}])
    return jsonify([{"cid":obj_data['cid'],"name" : obj_data['first_name'], "last_name" : obj_data['last_name']} for obj_data in all_users])