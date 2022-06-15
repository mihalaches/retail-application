import imp
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
from products.test_product import test
from products.carts import cart
from admin.view_orders import view_orders
from admin.login import login_admin
from admin.logout import logout_admin
from admin.all_users import all_users
from admin.all_products import all_products