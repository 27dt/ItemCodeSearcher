import sys
import sqlite3

def rebuild_table():
    # Nukes the current items table and creates it again.
    # Note: a unique identifier is used on item_id to prevent duplicates.
    conn = sqlite3.connect('db/items.db')
    cur = conn.cursor()
    
    try:
        cur.execute("DROP TABLE items")
    except:
        print("Note: Item table doesn't already exist")
    finally:
        cur.execute(
            """CREATE TABLE items (
                item_id     int,
                name        text,
                category    text,
                price       real,
                unique      (item_id)
        
                )""")
        
    conn.commit()
    conn.close()

def reload_default():
    # One-time helper function that reloads default table values from backup txt file.
    # Opens file and reads entries into an array, for db insertion.
    conn = sqlite3.connect('db/items.db')
    cur = conn.cursor()

    fhndl = open("default/item_codes.txt", "r")
    
    itemarray = []

    # Reads line and splits at comma, then adds line to dictionary, and stript \n character.
    for line in fhndl:
        itemCode, itemName, itemCat, itemPrice = line.split(",")
        itemCode = int(itemCode)
        itemPrice = float(itemPrice)
        itemarray.append((itemCode, itemName, itemCat, itemPrice))

    # Closes file.
    fhndl.close()

    for item in itemarray:
        #print(item)
        cur.execute("INSERT INTO items VALUES (?, ?, ?, ?)", (item[0], item[1], item[2], item[3]))

    conn.commit()
    conn.close()