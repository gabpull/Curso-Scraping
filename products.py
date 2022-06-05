from multiprocessing import connection


from connecction import *

class Products:
    def __init__(self, name, amazon_url, ebay_url, amazon_price, ebay_price):
        self.name = name
        self.amazon_url = amazon_url
        self.ebay_url = ebay_url
        self.amazon_price = amazon_price
        self.ebay_price = ebay_price

    def save_products(self):
        try:
            conn = connect()
            cursor = conn.cursor()
            sql = 'insert into Products (name, amazon_url, ebay_url, amazon_price, ebay_price) values (%s, %s, %s, %s, %s,)'
            datos = (self.name, self.amazon_url, self.ebay_url, self.amazon_price, self.ebay_price)
            cursor.exceute(sql, datos)
            conn.commit()
            conn.close()
            return "Productos Guardados"
        except mysql.Error as err:
            return "Ha ocurrido un error"
