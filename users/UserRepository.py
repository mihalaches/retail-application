from db.DbHandle import DbHandle

class UserRepository:

    def __init__(self) -> None:
        self.dbh = DbHandle()
        self.cursor = self.dbh.get_cursor()

    def get_all_users(self):
        query = "SELECT * FROM users"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def add_user(self,name,lname):
        query = "INSERT INTO users(name,lastname) VALUES (%s,%s) RETURNING *"
        self.cursor.execute(query,(name,lname))
        self.dbh.do_commit()
        return self.cursor.fetchall()

    def get_user_by_id(self,user_id):
        query = "SELECT * FROM users WHERE id = %s"
        self.cursor.execute(query,(user_id,))
        return self.cursor.fetchone()
