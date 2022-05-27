import imp
from application.app import app
from users.UserRepository import UserRepository
from flask import jsonify,request

@app.route("/adduser",methods = ["POST"])
def add_new_user():
    user_repository = UserRepository()
    name = request.json['name']
    lname = request.json['lastname']
    user_add = user_repository.add_user(name,lname)
    if user_add:
        return jsonify([{"id":obj_data[0],"name" : obj_data[1], "last_name" : obj_data[2]} for obj_data in user_add]),201
    return jsonify([{"message":"Error to insert!"}]),500