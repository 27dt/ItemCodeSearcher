import sys
import sqlite3

conn = sqlite3.connect('db/items.db')
cur = conn.cursor()

def create_item():
    pass
    
def delete_item():
    pass
    
def read_item():
    pass
    
def update_item():
    pass

def search_item(query):
    try:
        for row in cur.execute("SELECT * FROM items WHERE Name like '%" + str(query) + "%'"):
            print(row)

    except:
        print("Query isn't valid or doesn't match with an item.")

    finally:
        cur.execute("SELECT COUNT(*) FROM items")

def createItems(item_id, item_name, item_cat, item_price):
    pass

conn.commit()
conn.close()

'''
# Function that allows user to add new item to existing list.
def addItems(code, name):
    # Opens file for appending.
    fhandl = open("ItemCodes.txt", "a")

    # Checks if item code already exists.
    if str(code) in itemDict:
        print("Item code already exists, try again.")
    else:
        # Appends new code/name to the existing list.
        fhandl.write("\n"+str(code)+","+str(name))
        print("Item added successfully.")
    
    # Closes file, and outputs, and updates dictionary. 
    fhandl.close()
    createDict()

'''