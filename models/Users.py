from db.DbHandle import DbHandle

class Users:

    def __init__(self,cid,email,role,first_name,last_name,password,registered_date,country,phone_number,vat):
        self.cid = cid
        self.email = email
        self.role = role
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.registered_date = registered_date
        self.country = country
        self.phone_number = phone_number
        self.vat = vat

    