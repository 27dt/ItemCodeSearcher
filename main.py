import sqlite3
from tkinter import *
from tkinter import ttk

from db.items_queries import *
from db.models import DBConn, Item
from default.load_default import *

#------DB CONNECTION------#
db = DBConn(sqlite3.connect('db/items.db'))

#------SUPPORT FUNCS------#
# Restore DB: Calls rebuild_table and restore_default from default table, to restore DB to its original settings
def restore_db():
    rebuild_table(db)
    reload_default(db)

# About: Displays program name, author, and libraries used to create
def about():
    about_window = Tk()
    about_window.title("About")
    about_window.geometry("300x100")
    about_window.resizable(False, False)
    title = Label(about_window, text="Meat Department Management System (2023-2024)\n").pack()
    author = Label(about_window, text="Created By: Daniel Trakas\n").pack()     
    info =  Label(about_window, text="Created In: Python, SQLite3, Tkinter").pack()

def refresh():
    result = get_all_items(db)
    return result

def add():
    pass

def update():
    pass

def delete():
    pass

# NOT IMPLEMENTED: Light Dark Mode: Toggle from Light to Dark mode in system.----------------------------------------------------------------
# WILL INVOLVE SETTING GLOBAL VARIABLES FOR COLORS OF BUTTONS, TEXT BOXES, FONTS, ETC. DO THIS LATER-----------------------------------------
def light_dark_mode():
    pass

def item_selected(event):
    print("yuh")

#---------TKINTER---------#
root = Tk()
root.title("Meat Department Management System")
root.geometry("600x600")
root.resizable(False, False)

# Top Menu
menu_bar = Menu(root)

# File Menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Restore DB", command=restore_db)
file_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Toggle Light/Dark Mode", command=light_dark_mode)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Window Tab Controls
tab_control = ttk.Notebook(root)

item_tab = ttk.Frame(tab_control)
search_tab = ttk.Frame(tab_control)
tab_control.add(item_tab, text='Item Management')
tab_control.add(search_tab, text='Search/Lookup')

tab_control.pack(expand=1, fill="both")

# Item Tab
item_frame = Frame(item_tab)
item_frame.pack(pady=10)
#item_frame.grid(column=0, row=0)

item_scroll = Scrollbar(item_frame)
#item_scroll.pack(side=RIGHT, fill=Y)
item_scroll.grid(row=0, column=1, sticky='ns')

item_tree = ttk.Treeview(item_frame, yscrollcommand=item_scroll.set, selectmode=BROWSE)
#item_tree.pack()
item_tree.grid(column=0, row=0, pady=10)
item_tree.bind('<<TreeviewSelect>>', item_selected)

item_scroll.config(command=item_tree.yview)
    
item_tree['columns'] = ("ID", "Name", "Category", "Price")

item_tree.column("#0", width=50, minwidth=25)
item_tree.column("ID", anchor=W, width=60)
item_tree.column("Name", anchor=W, width=160)
item_tree.column("Category", anchor=W, width=120)
item_tree.column("Price", anchor=W, width=50)

item_tree.heading("#0", text="Label", anchor=W)
item_tree.heading("ID", text="Item ID", anchor=W)
item_tree.heading("Name", text="Name", anchor=CENTER)
item_tree.heading("Category", text="Category", anchor=W)
item_tree.heading("Price", text="Price", anchor=W)

result = refresh()

for i in range(0, len(result)):
    item_tree.insert(parent='', index='end', iid=i, text="Item", values=(result[i].item_id, str(result[i].name), str(result[i].category), result[i].price))

buttons_frame = Frame(item_tab)
#buttons_frame.grid(column=0, row=2)
buttons_frame.pack()

refresh_items_button = Button(buttons_frame, text="Refresh", command=refresh)
refresh_items_button.grid(row=0, column=0)

add_item_button = Button(buttons_frame, text="Add", command=add)
add_item_button.grid(row=0, column=1, padx=10)

update_item_button = Button(buttons_frame, text="Update", command=update)
update_item_button.grid(row=0, column=2)

delete_item_button = Button(buttons_frame, text="Delete", command=delete)
delete_item_button.grid(row=0,column=3, padx=10)






# Search Tab
search_label = Label(search_tab, text="Please enter a search query below:").place(relx=0.5, rely=0.1, anchor=CENTER)
search_box = Entry(search_tab, width=50).place(relx=0.5, rely=0.2, anchor=CENTER)

search_button = Radiobutton(search_tab, text="Search").grid(column=0, row=1)







root.config(menu=menu_bar)
root.mainloop()


'''

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

# Delete Item
def delete_items():
    item = Item(int(itemid_box.get()), name_box.get(), category_box.get(), float(price_box.get()))
    delete_item(db, item.item_id)

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

delete_item_button = Button(root, text="Delete Item", command=delete_items)
delete_item_button.grid(row=6, column=1)

root.mainloop()

db.conn.close()
'''