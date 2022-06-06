from math import prod


class Orders:

    def __init__(self,order_id,cid,products: list,ordered_date) -> None:
        self._order_id = order_id
        self._cid = cid
        self._products = products
        self._ordered_date = ordered_date
    
    @property
    def order_id(self):
        return self._order_id
    
    @order_id.setter
    def order_id(self,order_id):
        self._order_id = order_id
    
    @property
    def cid(self):
        return self._cid
    
    @cid.setter
    def cid(self,cid):
        self._cid = cid
    
    @property
    def products(self):
        return self._products
    
    @products.setter
    def products(self,products):
        self._products = products
    
    @property
    def ordered_date(self):
        return self._ordered_date
    
    @ordered_date.setter
    def ordered_date(self,ordered_date):
        self._ordered_date = ordered_date

    def __str__(self) -> str:
        return "Order id : {}".format(self.order_id)

    def __repr__(self) -> str:
        return "Order id : {}".format(self.order_id)