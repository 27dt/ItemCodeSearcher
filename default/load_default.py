def rebuild_table(conn, cur):
    # Nukes the current items table and creates it again.
    # Note: a unique identifier is used on item_id to prevent duplicates.
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

def reload_default(conn, cur):
    # One-time helper function that reloads default table values from backup txt file.
    # Opens file and reads entries into an array, for db insertion.
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

    try:
        for item in itemarray:
            cur.execute("INSERT INTO items VALUES (?, ?, ?, ?)", (item[0], item[1], item[2], item[3]))
    except:
        print("Error: Item(s) already exist. Please rebuild table before trying again.\n")

    conn.commit()