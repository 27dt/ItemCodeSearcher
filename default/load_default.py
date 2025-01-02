from db.models import DBConn, Item

def rebuild_table(db: DBConn): 
    # Nukes the current items table and creates it again.
    # Note: a unique identifier is used on item_id to prevent duplicates.
    try:
        db.cur.execute("DROP TABLE items")
    except:
        print("Note: Item table doesn't already exist. Will continue.")
    finally:
        db.cur.execute(
            """CREATE TABLE items (
                item_id     int,
                name        text,
                category    text,
                price       real,
                unique      (item_id)
        
                )""")
        
    db.conn.commit()
    print("Database has been cleared and rebuilt.")

def reload_default(db: DBConn):
    # One-time helper function that reloads default table values from backup txt file.
    # Opens file and reads entries into an array, for db insertion.
    fhndl = open("default/item_codes.txt", "r")
    
    itemArray = []

    # Reads line and splits at comma, then adds line to dictionary, and stript \n character.
    for line in fhndl:
        item_id, name, category, price = line.split(",")
        itemArray.append(Item(int(item_id), name, category, float(price)))

    # Closes file.
    fhndl.close()

    try:
        for item in itemArray:
            db.cur.execute("INSERT INTO items VALUES (?, ?, ?, ?)", (item.item_id, item.name, item.category, item.price))
    except:
        print("Error: Item(s) already exist. Please rebuild table before trying again.\n")

    db.conn.commit()
    print ("Database has been reloaded with default values.")