from db.DbHandle import DbHandle

class Products:

    def __init__(self,pid,product_name,product_category,product_price,guaranty,product_details,product_image):
        self._pid = pid
        self._product_name = product_name
        self._product_category = product_category
        self._product_price = product_price
        self._guaranty = guaranty
        self._product_details = product_details
        self._product_image = product_image

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self,pid):
        self._pid = pid

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

    def __str__(self) -> str:
        return "Product id : {}".format(self.pid)

    def __repr__(self) -> str:
        return "Product id : {}".format(self.pid)

    def serialize(self):
        return {
            "pid" : self.pid,
            "product_name" : self.product_name,
            "product_category" : self.product_category,
            "product_price" : self.product_price,
            "guaranty" : self.guaranty,
            "product_details" : self.product_details,
            "product_image" : self.product_image
        }    
