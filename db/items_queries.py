from db.models import *

def create_item(db: DBConn, item: Item):   
    try:
        db.cur.execute("INSERT INTO items VALUES (?, ?, ?, ?)", (item.item_id, item.name, item.category, item.price))
        db.conn.commit()

        print("Item created successfully:")
        print(item, "\n")
    except:
        print("Create Error: Invalid data or item ID already exists.\n")
        return

def delete_item(db: DBConn, item_id: int):
    try:
        db.cur.execute("DELETE FROM items WHERE item_id = {0}".format(item_id))
        db.conn.commit()

        print("Item ID: " + str(item_id) + " deleted successfully.\n")
    except:
        print("Delete Error: Invalid data or item ID doesn't exist.\n")
        return

def read_item(db: DBConn, item_id: int) -> Item:
    try:
        request = db.cur.execute("SELECT * FROM items WHERE item_id = {0}".format(item_id)).fetchone()
        response = Item(request[0], request[1], request[2], request[3])
        print(response, "\n")
        return response
    except:
        print("Read Error: Invalid data or item ID doesn't exist.\n")
        return
    
def update_item(db: DBConn, item: int):
    try:
        db.cur.execute("UPDATE items SET name = '{0}', category = '{1}', price = '{2}' WHERE item_id = '{3}'"
                       .format(item.name, item.category, item.price, item.item_id))
        db.conn.commit()

        print("Item updated successfully:")
        print(item, "\n")
    except:
        print("Update Error: Invalid data or item ID already exists.\n")
        return

def search_item(db: DBConn, query: str):
    try:
        response = []
        for row in db.cur.execute("SELECT * FROM items WHERE name like '%" + str(query) + "%'"):
            request = Item(row[0], row[1], row[2], row[3])
            print(request)
            response.append(request)
        print("{0} Result(s) found.".format(len(response)))
        return response
    except:
        print("Search Error: Query doesn't match with an item.\n")
        return
    
def get_all_items(db: DBConn):
    try:
        response = []
        for row in db.cur.execute("SELECT * FROM items"):
            request = Item(row[0], row[1], row[2], row[3])
            print(request)
            response.append(request)
        
        return response
    except:
        print("Error.\n")