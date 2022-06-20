from users.UserRepository import UserRepository
from libs.token import jwt_token
from libs.messages import Messages
from libs.CMailHandler import CMailHandler
from libs.messages import Messages


class reset_password:

    _user_repo = UserRepository()

    @classmethod
    def send_reset_token(cls, email, url, path_param):
        user_exist = cls._user_repo.get_user("email", email)
        if not user_exist:
            return Messages.INVALID_EMAIL
        cls._user_repo.update_user("active_token",user_exist.cid,'1')
        generated_token = jwt_token.encode(cid=user_exist.cid)
        url_created = url + "?{}=".format(path_param) + generated_token
        subject = Messages.RESET_MAIL_SUBJECT
        content = Messages.RESET_MAIL_CONTENT.format(link_reset=url_created)
        CMailHandler().send(email, subject, content)
        return Messages.RESET_PASSWORD_MAIL_SEND
