class Users:

    def __init__(self,cid,email,role,first_name,last_name,password,registered_date,country,phone_number,vat,deposit,cart):
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
        self._cart = cart

    @property
    def cid(self):
        return self._cid
    
    @cid.setter
    def cid(self,cid):
        self._cid = cid

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self,email):
        self._email = email

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self,role):
        self._role = role

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self,first_name):
        self._first_name = first_name

    @property    
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self,last_name):
        self._last_name = last_name

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,password):
        self._password = password

    @property
    def registered_date(self):
        return self._registered_date

    @registered_date.setter
    def registered_date(self,registered_date):
        self._registered_date = registered_date

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self,country):
        self._country = country

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self,phone_number):
        self._phone_number = phone_number

    @property
    def vat(self):
        return self._vat

    @vat.setter
    def vat(self,vat):
        self._vat = vat

    @property
    def deposit(self):
        return self._deposit

    @deposit.setter
    def deposit(self,deposit):
        self._deposit = deposit
    
    @property
    def cart(self):
        return self._cart

    @cart.setter
    def cart(self,cart):
        self._cart = cart
    
    def __str__(self) -> str:
        return "User cid : {}".format(self.cid)

    def __repr__(self) -> str:
        return "User cid : {}".format(self.cid)

    def serialize(self):
        return {
            "cid" : self.cid,
            "email" : self.email,
            "role" : self.role,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "registered_date" : self.registered_date,
            "country" : self.country,
            "phone_number" : self.phone_number,
            "vat" : self.vat,
            "deposit" : self.deposit,
            "cart" : self.cart
        }                            


    