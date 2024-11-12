# Item class for passing to DB
class Item:
    def __init__(self, item_id, name, category, price):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.price = price

# Class for SQLite DB: Cursor and Connection
class DBConn:
    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()