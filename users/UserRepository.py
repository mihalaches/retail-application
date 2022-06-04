from tkinter import N
from db.DbHandle import DbHandle
import bcrypt
from datetime import datetime
from models.Users import Users
from products.ProductRepository import ProductRepository

class UserRepository:

    def __init__(self) -> None:
        self.dbh = DbHandle()
        self.cursor = self.dbh.get_cursor()
        self.product_repo = ProductRepository()

    def get_all_users(self):
        query = "SELECT * FROM customers INNER JOIN deposit ON deposit.user_cid = customers.cid INNER JOIN roles ON customers.role = roles.id"
        self.cursor.execute(query)
        data_fetch = self.cursor.fetchall()
        list_users = []
        for element in data_fetch:
            list_users.append(Users(element['cid'],element['email'],element['role_name'],element['first_name'],element['last_name'],
            element['password'],element['registered_date'],
            element['country'],element['phone_number'], element['vat'],element['amount']))
        print(list_users)
        return list_users

    def add_user(self,email,first_name,last_name,password,country,phone_number):
        query = """
            INSERT INTO
                customers(
                    email,
                    role,
                    first_name,
                    last_name,
                    password,
                    registered_date,
                    country,
                    phone_number,
                    vat
                )
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
            RETURNING
                *
        """
        query_deposit = """
            INSERT INTO
                deposit(
                    user_cid,
                    amount,
                    sync_date
                )
                VALUES(%s,%s,%s)
        """
        hash_pwd = bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")
        vat = 19.0
        try:
            self.cursor.execute(query,(email,2,first_name,last_name,hash_pwd,datetime.now(),country,phone_number,vat))
            data_fetch = self.cursor.fetchone()
            self.cursor.execute(query_deposit,(data_fetch['cid'],0,datetime.now()))
        except Exception as ex:
            print(ex.args)
            return None
        self.dbh.do_commit()
        return data_fetch

    def get_user(self,param,value):
        query = "SELECT * FROM customers INNER JOIN deposit ON deposit.user_cid = customers.cid INNER JOIN roles ON customers.role = roles.id WHERE customers.{} = %s".format(param)
        self.cursor.execute(query,(value,))
        data_fetch = self.cursor.fetchone()
        query_orders = "SELECT id,products FROM customers_orders WHERE user_cid = %s"
        list_products = []
        if data_fetch:
            self.cursor.execute(query_orders,(data_fetch['cid'],))
            data_fetch_orders = self.cursor.fetchall()
            for prod in data_fetch_orders:
                list_products.append(self.product_repo.get_by_id(prod['products'],prod['id']))
        if data_fetch:
            return Users(data_fetch['cid'],data_fetch['email'],data_fetch['role_name'],data_fetch['first_name'],
                    data_fetch['last_name'],data_fetch['password'],data_fetch['registered_date'],data_fetch['country'],
                    data_fetch['phone_number'], data_fetch['vat'],data_fetch['amount'],list_products)
        return None

    def update_deposit(self,cid,new_amount):
        query = "UPDATE deposit SET amount = %s WHERE user_cid = %s"
        try:
            self.cursor.execute(query,(new_amount,cid))
        except Exception as ex:
            print(ex.args)
            return False
        self.dbh.do_commit()
        print(cid,new_amount)
        print("assdasdaasd")
        return True