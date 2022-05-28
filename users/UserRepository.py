from db.DbHandle import DbHandle
import bcrypt
from datetime import datetime

class UserRepository:

    def __init__(self) -> None:
        self.dbh = DbHandle()
        self.cursor = self.dbh.get_cursor()

    def get_all_users(self):
        query = "SELECT * FROM customers"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def add_user(self,email,first_name,last_name,password,country,phone_number):
        query = """
            INSERT INTO
                customers(
                    email,
                    role,
                    first_name,
                    last_name,
                    password,
                    registerd_date,
                    country,
                    phone_number,
                    vat
                )
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
            RETURNING
                *
        """
        hash_pwd = bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt())
        vat = 19.0
        self.cursor.execute(query,(email,1,first_name,last_name,hash_pwd,datetime.now(),country,phone_number,vat))
        self.dbh.do_commit()
        return self.cursor.fetchall()

    def get_user_by_id(self,user_id):
        query = "SELECT * FROM customers WHERE cid = %s"
        self.cursor.execute(query,(user_id,))
        return self.cursor.fetchone()
