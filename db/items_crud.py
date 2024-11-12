def create_item(db, item):   
    try:
        db.cur.execute("INSERT INTO items VALUES (?, ?, ?, ?)", (item.item_id, item.name, item.category, item.price))
        db.conn.commit()

        print("Item created successfully: \n")
        print("ID: " + str(item.item_id) + " Name: " + str(item.name) + " Category: " + str(item.category) + " Price: " + str(item.price) + "\n")
    except:
        print("Create Error: Invalid data or item ID already exists.\n")
        return

def delete_item(db, item_id):
    try:
        db.cur.execute("DELETE FROM items WHERE item_id = " + str(item_id))
        db.conn.commit()

        print("Item ID: " + str(item_id) + " deleted successfully.\n")
    except:
        print("Delete Error: Invalid data or item ID doesn't exist.\n")
        return

def read_item(db, item_id):
    try:
        for row in db.cur.execute("SELECT * FROM items WHERE item_id = " + str(item_id)):
            print(row)
    except:
        print("Read Error: Invalid data or item ID doesn't exist.\n")
        return
    
def update_item(db, item):
    try:
        db.cur.execute("UPDATE items SET name = '" + str(item.name) + "', category = '" + str(item.category) + "', price = " + str(item.price) + " WHERE item_id = " + str(item.item_id))
        db.conn.commit()

        print("Item updated successfully: \n")
        print("ID: " + str(item.item_id) + " Name: " + str(item.name) + " Category: " + str(item.cat) + " Price: " + str(item.price) + "\n")
    except:
        print("Update Error: Invalid data or item ID already exists.\n")
        return

def search_item(db, query):
    try:
        for row in db.cur.execute("SELECT * FROM items WHERE name like '%" + str(query) + "%'"):
            print(row)
    except:
        print("Search Error: Query doesn't match with an item.\n")
        return
    #finally:
    #cur.execute("SELECT COUNT(*) FROM items")
    #cur.execute("SELECT COUNT() FROM items WHERE Name like '%" + str(query) + "%'")
    #print(str(cur.fetchone()) + " results found.\n")
    
def get_all_items(db):
    try:
        for row in db.cur.execute("SELECT * FROM items"):
            print(row)
    except:
        print("Error.")