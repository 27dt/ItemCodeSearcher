# Item class for passing to DB
class Item:
    def __init__(self, item_id: int, name: str, category: str, price: int):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return "ID: {0} Name: {1} Category: {2} Price: {3}".format(self.item_id, self.name, self.category, self.price)
        
# Class for SQLite DB: Cursor and Connection
class DBConn:
    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()