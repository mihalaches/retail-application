from db.DbHandle import DbHandle
from models.Users import Users
from models.Products import Products
from datetime import datetime
from uuid import uuid4

class ProductRepository:

    def __init__(self) -> None:
        self.dbh = DbHandle()
        self.cursor = self.dbh.get_cursor()

    def get_all(self):
        query = "SELECT products.id,products_category.category_name,products.product_name,products.product_price,products.guaranty,products.product_details,products.product_image FROM products INNER JOIN products_category ON products_category.id = products.product_category WHERE products.disabled = '0'"
        self.cursor.execute(query)
        data_fetch = self.cursor.fetchall()
        list_products = []
        if data_fetch:
            for prod in data_fetch:
                list_products.append(Products(prod['id'], prod['product_name'], prod['category_name'], prod['product_price'], prod['guaranty'],
                                              prod['product_details'], prod['product_image'], "Undef"))
            list_products.sort(key = lambda prod : prod.pid)
            return list_products
        return None

    def get_by_id(self, product_id, cart_product_id):
        query = "SELECT products.id,products_category.category_name,products.product_name,products.product_price,products.guaranty,products.product_details,products.product_image FROM products INNER JOIN products_category ON products_category.id = products.product_category WHERE products.id = %s"
        self.cursor.execute(query, (product_id,))
        data_fetch = self.cursor.fetchone()
        if data_fetch:
            return Products(data_fetch['id'], data_fetch['product_name'], data_fetch['category_name'], data_fetch['product_price'], data_fetch['guaranty'],
                            data_fetch['product_details'], data_fetch['product_image'], cart_product_id)
        return None

    def add_to_cart(self, product_id, cid):
        query = """
            INSERT INTO
                customers_orders(
                    user_cid,
                    products,
                    active,
                    inserted_date
                )
            VALUES(%s,%s,1,%s)
        """
        try:
            self.cursor.execute(query, (cid, product_id,datetime.now()))
        except Exception as ex:
            print(ex.args)
            return False
        self.dbh.do_commit()
        return True

    def delete_from_cart(self, cart_p_id):
        query = """
            UPDATE
                customers_orders
            SET
                active = '0'
            WHERE
                id = %s
        """
        try:
            self.cursor.execute(query, (cart_p_id,))
        except Exception as ex:
            print(ex.args)
            return False
        self.dbh.do_commit()
        return True

    def delete(self, pid):
        query = """
            UPDATE
                products
            SET
                disabled = '1'
            WHERE
                id = %s
        """
        query_cart = """
            UPDATE 
                customers_orders
            SET
                active = '0'
            WHERE
                products = %s
        """
        try:
            self.cursor.execute(query, (pid,))
            self.cursor.execute(query_cart, (pid,))
        except Exception as ex:
            print(ex.args)
            return False
        self.dbh.do_commit()
        return True

    def delete_cart_products_by_cid(self, cid, ordered = None):
        query = """
            UPDATE
                customers_orders
            SET
                active = '0'
            WHERE
                user_cid = %s
        """
        if ordered:
            query = """
                UPDATE
                    customers_orders
                SET
                    active = '0',
                    ordered_date = '{order_date}',
                    order_id = '{order_id}'
                WHERE
                    user_cid = %s
                AND
                    active = '1'
            """.format(order_date = datetime.now(), order_id=str(uuid4()))
        try:
            self.cursor.execute(query, (cid,))
        except Exception as ex:
            print(ex.args)
            return False
        self.dbh.do_commit()
        return True

    def sort_by_category(self, category_name):
        query = "SELECT products.id,products_category.category_name,products.product_name,products.product_price,products.guaranty,products.product_details,products.product_image FROM products INNER JOIN products_category ON products_category.id = products.product_category WHERE products_category.category_name = %s AND products.disabled = '0'"
        self.cursor.execute(query,(category_name,))
        data_fetch = self.cursor.fetchall()
        list_products = []
        if data_fetch:
            for prod in data_fetch:
                list_products.append(Products(prod['id'], prod['product_name'], prod['category_name'], prod['product_price'], prod['guaranty'],
                                              prod['product_details'], prod['product_image'], "Undef"))
            return list_products
        return None

    def get_product_category(self):
        query = "SELECT * FROM products_category"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def add_new_category(self,product_category):
        query = """
            INSERT INTO
                products_category(
                    category_name
                )
                VALUES
                (%s)
        """
        try:
            self.cursor.execute(query, (product_category,))
        except Exception as ex:
            print(ex.args)
            return False
        self.dbh.do_commit()
        return True
    
    def get_category_id_by_name(self,category_name):
        query = "SELECT id FROM products_category WHERE category_name = %s"
        self.cursor.execute(query,(category_name,))
        return self.cursor.fetchone()['id']

    def update(self,product_name,product_category,product_price,product_guaranty,product_details,product_id,product_image=None):
        category_id = self.get_category_id_by_name(product_category)
        if product_image:
            query = """
                UPDATE
                    products
                SET
                    product_name = %s,
                    product_category = %s,
                    product_price = %s,
                    guaranty = %s,
                    product_details = %s,
                    product_image = %s
                WHERE
                    id = %s
            """
        else:
            query = """
                UPDATE
                    products
                SET
                    product_name = %s,
                    product_category = %s,
                    product_price = %s,
                    guaranty = %s,
                    product_details = %s
                WHERE
                    id = %s
            """
        try:
            if product_image:
                self.cursor.execute(query, (product_name,category_id,product_price,product_guaranty,product_details,product_image,product_id))
            else:
                self.cursor.execute(query, (product_name,category_id,product_price,product_guaranty,product_details,product_id))
        except Exception as ex:
            print(ex.args)
            return False
        self.dbh.do_commit()
        return True

    def add(self,product_name,product_category,product_price,product_guaranty,product_details,product_image):
        category_id = self.get_category_id_by_name(product_category)
        query = """
            INSERT INTO
                products(
                    product_name,
                    product_category,
                    product_price,
                    guaranty,
                    product_details,
                    product_image
                )
                VALUES
                (%s,%s,%s,%s,%s,%s)
        """
        try:
            self.cursor.execute(query, (product_name,category_id,product_price,product_guaranty,product_details,product_image,))
        except Exception as ex:
            print(ex.args)
            return False
        self.dbh.do_commit()
        return True
        