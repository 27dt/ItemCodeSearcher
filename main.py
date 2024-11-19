import sqlite3
from tkinter import *

from db.items_queries import *
from db.models import DBConn, Item
from default.load_default import *

#------DB CONNECTION------#
db = DBConn(sqlite3.connect('db/items.db'))

#--------TKINTER UI-------#
root = Tk()
root.title('Item Management System')
root.geometry('400x400')

#------SUPPORT FUNCS------#
# Clear fields
def clear_fields():
    itemid_box.delete(0, END)
    name_box.delete(0, END)
    category_box.delete(0, END)
    price_box.delete(0, END)

# Add Item
def add_item():
    item = Item(int(itemid_box.get()), name_box.get(), category_box.get(), float(price_box.get()))
    create_item(db, item)

# List All Items
def list_items():
    list_items_window = Tk()
    list_items_window.title("List All Items")
    list_items_window.geometry("400x600")

    #result = get_all_items()

    #for item in result:
        


#--------TKINTER UI-------#
# Label
title_label = Label(root, text="Item Management System V2.0", font="Arial")
title_label.grid(row=0, column=0, columnspan=2, pady="10")

# Text for fields
itemid_label = Label(root, text="Item ID: ").grid(row=1, column=0, sticky=W, padx=10)
name_label = Label(root, text="Item Name: ").grid(row=2, column=0, sticky=W, padx=10)
category_label = Label(root, text="Item Category: ").grid(row=3, column=0, sticky=W, padx=10)
price_label = Label(root, text="Item Price: ").grid(row=4, column=0, sticky=W, padx=10)

# Forms for fields
itemid_box = Entry(root)
itemid_box.grid(row=1, column=1)

name_box = Entry(root)
name_box.grid(row=2, column=1)

category_box = Entry(root)
category_box.grid(row=3, column=1)

price_box = Entry(root)
price_box.grid(row=4, column=1)

# Buttons
add_item_button = Button(root, text="Add Item", command=add_item)
add_item_button.grid(row=5, column=0, padx=10, pady=10)

clear_fields_button = Button(root, text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=5, column=1)

list_all_items_button = Button(root, text="List All Items", command=list_items)
list_all_items_button.grid(row=6, column=0)

root.mainloop()

db.conn.close()