import unittest
import sqlite3

from db.items_queries import *
from db.models import DBConn, Item
from default.load_default import *

#------DB CONNECTION------#
db = DBConn(sqlite3.connect('db/items.db'))

#------FACTORY RESET------#
#rebuild_table(db)
#reload_default(db)

#----------TESTS----------#
#create_item(db, Item(12345, "Daniel", "Human", 100))
#delete_item(db, 12345)
#read_item(db, 14218)
#update_item(db, Item(12345, "Dannn0", "Creature", 3.33))
#search_item(db, "chicken")
#get_all_items(db)

db.conn.close()
