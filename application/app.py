from flask import Flask

app = Flask(__name__)

SECRET_KEY = "fkjfsdlkhjsdkanhfasnhljfa"

app.secret_key = SECRET_KEY

from users.register import register
from users.get_all_users import get_all_users
from users.add_new_user import add_new_user
from users.login import login
from users.logout import logout
from products.products_list import products_list