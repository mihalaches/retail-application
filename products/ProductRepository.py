from db.DbHandle import DbHandle
from models.Users import Users
from models.Products import Products

class ProductRepository:

    def __init__(self) -> None:
        self.dbh = DbHandle()
        self.cursor = self.dbh.get_cursor()
    
    def get_by_id(self,product_id,cart_product_id):
        query = "SELECT * FROM products INNER JOIN products_category ON products_category.id = products.product_category WHERE products.id = %s"
        self.cursor.execute(query,(product_id,))
        data_fetch = self.cursor.fetchone()
        if data_fetch:
            return Products(data_fetch['id'],data_fetch['product_name'],data_fetch['category_name'],data_fetch['product_price'],data_fetch['guaranty'],
                    data_fetch['product_details'],data_fetch['product_image'],cart_product_id)
        return None

    def add_to_cart(self,product_id,cid):
        query = """
            INSERT INTO
                customers_orders(
                    user_cid,
                    products
                )
            VALUES(%s,%s)
        """
        try:
            self.cursor.execute(query,(cid,product_id))
        except Exception as ex:
            print(ex.args)
            return False
        self.dbh.do_commit()
        return True
    
    def delete_from_cart(self,cart_p_id):
        query = """
            DELETE FROM
                customers_orders
            WHERE
                id = %s
        """
        try:
            self.cursor.execute(query,(cart_p_id,))
        except Exception as ex:
            print(ex.args)
            return False
        self.dbh.do_commit()
        return True
