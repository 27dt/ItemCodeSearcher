def create_item(conn, cur, item_id, item_name, item_cat, item_price):   
    try:
        cur.execute("INSERT INTO items VALUES (?, ?, ?, ?)", (item_id, item_name, item_cat, item_price))
        conn.commit()

        print("Item created successfully: \n")
        print("ID: " + str(item_id) + " Name: " + str(item_name) + " Category: " + str(item_cat) + " Price: " + str(item_price) + "\n")
    except:
        print("Create Error: Invalid data or item ID already exists.\n")
        return

def delete_item(conn, cur, item_id):
    try:
        cur.execute("DELETE FROM items WHERE item_id = " + str(item_id))
        conn.commit()

        print("Item ID: " + str(item_id) + " deleted successfully.\n")
    except:
        print("Delete Error: Invalid data or item ID doesn't exist.\n")
        return

def read_item(cur, item_id):
    try:
        for row in cur.execute("SELECT * FROM items WHERE item_id = " + str(item_id)):
            print(row)
    except:
        print("Read Error: Invalid data or item ID doesn't exist.\n")
        return
    
def update_item(conn, cur, item_id, item_name, item_cat, item_price):
    try:
        cur.execute("UPDATE items SET name = '" + str(item_name) + "', category = '" + str(item_cat) + "', price = " + str(item_price) + " WHERE item_id = " + str(item_id))
        conn.commit()

        print("Item updated successfully: \n")
        print("ID: " + str(item_id) + " Name: " + str(item_name) + " Category: " + str(item_cat) + " Price: " + str(item_price) + "\n")
    except:
        print("Update Error: Invalid data or item ID already exists.\n")
        return

def search_item(cur, query):
    try:
        for row in cur.execute("SELECT * FROM items WHERE name like '%" + str(query) + "%'"):
            print(row)
    except:
        print("Search Error: Query doesn't match with an item.\n")
        return

    #finally:
        #cur.execute("SELECT COUNT(*) FROM items")