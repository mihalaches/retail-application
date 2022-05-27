from db.DbHandle import DbHandle

class Users:

    def __init__(self,cid,email,role,first_name,last_name,password,registered_date,country,phone_number,vat,deposit):
        self._cid = cid
        self._email = email
        self._role = role
        self._first_name = first_name
        self._last_name = last_name
        self._password = password
        self._registered_date = registered_date
        self._country = country
        self._phone_number = phone_number
        self._vat = vat
        self._deposit = deposit

    @property
    def cid(self):
        return self._cid
    
    @cid.setter
    def cid(self,cid):
        self._cid = cid

    