from db.DbHandle import DbHandle
import bcrypt
from datetime import datetime
from models.Users import Users

class UserRepository:

    def __init__(self) -> None:
        self.dbh = DbHandle()
        self.cursor = self.dbh.get_cursor()

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
        hash_pwd = bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt())
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

    def get_user_by_id(self,user_id):
        query = "SELECT * FROM customers WHERE cid = %s"
        self.cursor.execute(query,(user_id,))
        return self.cursor.fetchone()
