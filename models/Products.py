from db.DbHandle import DbHandle

class Products:

    def __init__(self,product_name,product_category,product_price,guaranty,product_details,product_image):
        self._product_name = product_name
        self._product_category = product_category
        self._product_price = product_price
        self._guaranty = guaranty
        self._product_details = product_details
        self._product_image = product_image

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self,product_name):
        self._product_name = product_name

    @property
    def product_category(self):
        return self._product_category

    @product_category.setter
    def product_category(self,product_category):
        self._product_category = product_category

    @property
    def product_price(self):
        return self._product_price

    @product_price.setter
    def product_price(self,product_price):
        self._product_price = product_price

    @property
    def guaranty(self):
        return self._guaranty

    @guaranty.setter
    def guaranty(self,guaranty):
        self._guaranty = guaranty

    @property
    def product_details(self):
        return self._product_details

    @product_details.setter
    def product_details(self, product_details):
        self._product_details = product_details

    @property
    def product_image(self):
        return self._product_image

    @product_image.setter
    def product_image(self,product_image):
        self._product_image = product_image                                                    

