import sys
import sqlite3

from tkinter import *

from db.items_crud import *
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
#read_item(db, 12345)
#update_item(db, Item(12345, "Dannn0", "Creature", 3.33))
#search_item(db, "dan")
#get_all_items(db)

db.conn.close()

























'''

# Root Window
root = Tk()

# Title and Dimensions
root.title("ItemCodeSearcher")
root.geometry('400x200')

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar 

# Menu Bar
menu = Menu(root)

# Item in Menu Bar
item = Menu(menu)
item.add_command(label='New')

# Item can be found under File
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

# Label
lbl = Label(root, text = "yuh")
lbl.grid()

txt = Entry(root, width=10)
txt.grid(column=1, row=0)

def clicked():
    res = "you wrote " + txt.get() 
    lbl.configure(text = res)

btn = Button(root, text = "click me", fg = "red", command=clicked)
btn.grid(column=2, row=0)

root.mainloop()

'''