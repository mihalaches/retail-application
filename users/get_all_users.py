import imp
from application.app import app
from users.UserRepository import UserRepository
from flask import jsonify, request, session
from libs.token import check_auth
import base64


@app.route("/allusers",methods = ["POST","GET"])
@check_auth
def get_all_users(user):
    user_repository = UserRepository()
    all_users = user_repository.get_all_users()
    if request.args.get("id"):
        specific_user = user_repository.get_user_by_id(request.args.get("id"))
        if specific_user:
            return jsonify(specific_user.serialize())
        else:
            return jsonify({"message":"No user with that id!"}),404
    return jsonify([user.serialize() for user in all_users])