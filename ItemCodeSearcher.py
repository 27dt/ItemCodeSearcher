import sys
import sqlite3

from default.load_default import *
from db.items_crud import *

#------DB CONNECTION------#
conn = sqlite3.connect('db/items.db')
cur = conn.cursor()

#------FACTORY RESET------#
#rebuild_table(conn, cur)
#reload_default(conn, cur)

#----------TESTS----------#
#create_item(conn, cur, 12345, "Daniel", "Human", 100)
#delete_item(conn, cur, 12345)
#read_item(cur, 12345)
#update_item(conn, cur, 12345, "Dannn0", "Creature", 3.33)
#search_item(cur, "dan")

conn.commit()

#--------PRINT ALL--------#
for row in cur.execute("SELECT * FROM items"):
    print(row)



'''
def readItems(query):
    print("---------- SEARCHES FOR \""+query+"\" ----------")

    try:
        for row in cur.execute("SELECT * FROM items WHERE Name like '%" + str(query) + "%'"):
            print(row)

    except:
        print("Query isn't valid or doesn't match with an item.")

    finally:
        cur.execute("SELECT COUNT() FROM items WHERE Name like '%" + str(query) + "%'")
        print(str(cur.fetchone()) + " results found.")
'''

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


# Creates dictionary, outputs options, and prompts a user selection.
createDict()
print("Please input a selection and press enter:")

# Initializes user input variable.
userInput = ""

# Loop continues while input is not QUIT, to allow for multiple options.
while userInput != "QUIT":
    print("1) Search for an item.")
    print("2) Add a new item to the system")
    userInput = input("Type \"QUIT\" at any time to exit.\n")

    # If 1 is input, the item search option is displayed.
    if userInput == '1':
        print("Type \"BACK\" to return to the main menu.")
        print("Enter a query to search for.")
        searchQuery = input()

        # Goes back if "BACK" is input, otherwises searches for user query.
        if searchQuery != "BACK":
            searchItems(searchQuery)
        else:
            continue
    
    # If 2 is input, the item add option is displayed.
    if userInput == '2':
        print("Type \"BACK\" to return to the main menu.")
        itemCode = input("Please enter the new item's code: ")
        itemName = input("Please enter the new item's name: ")

        # Goes back if "BACK" is input, otherwises adds item with user's code and name.
        if itemCode == "BACK":
            continue
        elif itemName == "BACK":
            continue
        else:
            # Verifies that an integer has been input for the item code.
            try:
                addItems(int(itemCode), itemName)
            except:
                print("Only integers are allowed for an item code.")

# Uses sys to terminate program if "QUIT" is input.
if userInput == "QUIT":
    sys.exit()
'''