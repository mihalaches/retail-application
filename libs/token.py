import jwt
from application.app import SECRET_KEY
from libs.exceptions import InvalidToken
from datetime import datetime, timedelta,timezone
from functools import wraps
from flask import session,redirect,url_for
from users.UserRepository import UserRepository

user_repo = UserRepository()

def check_auth(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        if not session.get("token"):
            session.clear()
            return redirect(url_for('login'))
        if not jwt_token.check_valability(session.get('token')):
            session.clear()
            return redirect(url_for('login'))
        decoded_token = jwt_token.decode(session['token'])
        user_found = user_repo.get_user("cid",decoded_token['cid'])
        if not user_found:
            return redirect(url_for('login')) 
        return function(user_found,*args,**kwargs)
    return wrapper

def no_login_req(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        try:
            decoded_token = jwt_token.decode(session['token'])
            user_found = user_repo.get_user("cid",decoded_token['cid'])
        except:
            user_found = None
        if session.get("token") and user_found:
            return redirect(url_for("get_all_users"))
        return function(*args,**kwargs)
    return wrapper


class jwt_token:

    @staticmethod
    def encode(**kwargs):
        kwargs['expiration'] = datetime.timestamp(datetime.now(tz=timezone.utc) + timedelta(minutes=30))
        return jwt.encode(kwargs,SECRET_KEY,algorithm="HS256")

    @staticmethod
    def decode(token):
        return jwt.decode(token,SECRET_KEY,algorithms=['HS256'])

    @staticmethod
    def check_valability(token) -> bool:
        decoded_token = jwt_token.decode(token=token)
        if not decoded_token['expiration']:
            raise InvalidToken("Token has no expire date!")
        if decoded_token['expiration'] < datetime.timestamp(datetime.now()):
            return False
        return True
