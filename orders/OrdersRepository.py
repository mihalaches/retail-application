from db.DbHandle import DbHandle
from models.Orders import Orders
from products.ProductRepository import ProductRepository
from users.UserRepository import UserRepository

class OrdersRepository:

    def __init__(self) -> None:
        self.dbh = DbHandle()
        self.cursor = self.dbh.get_cursor()
        self.prod_repo = ProductRepository()
        self.user_repo = UserRepository()

    def get_distinct(self):
        query = "SELECT DISTINCT order_id FROM customers_orders WHERE order_id != 'null'"
        self.cursor.execute(query=query)
        return self.cursor.fetchall()

    def get_all(self):
        list_orders = []
        order_date = None
        order_cid = None
        all_orders = self.get_distinct()
        query = "SELECT * FROM customers_orders WHERE order_id = %s"
        for order in all_orders:
            self.cursor.execute(query,(order['order_id'],))
            data_order = self.cursor.fetchall()
            product_list = []
            for element in data_order:
                product_list.append(self.prod_repo.get_by_id(element['products'],element['id']))
                order_date = element['ordered_date']
                order_cid = element['user_cid']
            list_orders.append(Orders(order['order_id'],self.user_repo.get_user("cid",order_cid),product_list,order_date))
        return list_orders

