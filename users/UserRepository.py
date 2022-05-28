from db.DbHandle import DbHandle
import bcrypt
from datetime import datetime
from models.Users import Users

class UserRepository:

    def __init__(self) -> None:
        self.dbh = DbHandle()
        self.cursor = self.dbh.get_cursor()

    def get_all_users(self):
        query = "SELECT * FROM customers INNER JOIN deposit ON deposit.user_cid = customers.cid"
        self.cursor.execute(query)
        data_fetch = self.cursor.fetchall()
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
            self.cursor.execute(query,(email,1,first_name,last_name,hash_pwd,datetime.now(),country,phone_number,vat))
            data_fetch = self.cursor.fetchone()
            self.cursor.execute(query_deposit,(data_fetch['cid'],0,datetime.now()))
        except Exception as ex:
            return None
        self.dbh.do_commit()
        return data_fetch

    def get_user_by_id(self,user_id):
        query = "SELECT * FROM customers WHERE cid = %s"
        self.cursor.execute(query,(user_id,))
        return self.cursor.fetchone()
