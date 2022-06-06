class Orders:

    def __init__(self, order_id, user, products: list, ordered_date) -> None:
        self._order_id = order_id
        self._user = user
        self._products = products
        self._ordered_date = ordered_date

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        self._order_id = order_id

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, products):
        self._products = products

    @property
    def ordered_date(self):
        return self._ordered_date

    @ordered_date.setter
    def ordered_date(self, ordered_date):
        self._ordered_date = ordered_date

    def __str__(self) -> str:
        return "Order id : {}".format(self.order_id)

    def __repr__(self) -> str:
        return "Order id : {}".format(self.order_id)
