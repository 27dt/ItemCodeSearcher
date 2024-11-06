import sys
import sqlite3

conn = sqlite3.connect('items.db')
cur = conn.cursor()

def rebuild_table():
    # Nukes the current items table and creates it again.
    # Note: a unique identifier is used on item_id to prevent duplicates.
    try:
        cur.execute("DROP TABLE items")
    except:
        print("item table doesn't already exist.")
    finally:
        cur.execute(
            """CREATE TABLE items (
                item_id     int,
                name        text,
                category    text,
                price       real,
                unique      (item_id)
        
                )""")

def reload_default():
    # One-time helper function that reloads default table values from backup txt file.
    # Opens file for reading and initializes dictionary.
    fhndl = open("ItemCodes.txt", "r")
    
    itemDict = {}
    itemarray = []

    # Reads line and splits at comma, then adds line to dictionary, and stript \n character.
    for line in fhndl:
        itemCode, itemName, itemCat, itemPrice = line.split(",")
        itemCode = int(itemCode)
        itemPrice = float(itemPrice)
        itemDict[itemCode] = [itemName, itemCat, itemPrice]

    # Closes file.
    fhndl.close()

    # Appends each item to itemarray
    for key in itemDict:
        itemarray.append((key, itemDict[key][0], itemDict[key][1], itemDict[key][2]))   

    # Uses itemarray to insert each item into the items table
    for key in itemDict:
        cur.execute("INSERT INTO items VALUES (?, ?, ?, ?)", (key, itemDict[key][0], itemDict[key][1], itemDict[key][2]))
        # PRINT STATEMENT BELOW IS FOR DEBUGGING
        #print("ID: " + str(key) + " NAME: " + itemDict[key][0] + " CAT: " + itemDict[key][1] + " PRICE: " + str(itemDict[key][2]) + "\n")





















'''
# Function that searches for user-input query.
def searchItems(query):
    print("---------- SEARCHES FOR \""+query+"\" ----------")
    results = 0

    # Loops through dictionary of items, appends matching items to list as tuple, and prints list.
    searchList = []

    for key in itemDict:
        # Uses string.casefold() for case insensitive comparison.
        if query.casefold() in itemDict[key].casefold():
            searchList.append((key,itemDict[key]))
            results += 1
    
    # Prints results.
    for i in range(0, len(searchList)):
        print(searchList[i])
    
    # Prints number of results found (in case none are found).
    print(results, "results found.")
 ''' 

def readItems(query):
    print("---------- SEARCHES FOR \""+query+"\" ----------")

    try:
        for row in cur.execute("SELECT * FROM items WHERE Name like '%" + str(query) + "%'"):
            print(row)

    except:
        print("Query isn't valid or doesn't match with an item.")

    finally:
        cur.execute("SELECT COUNT(*) FROM items")


#rebuild_table()
#reload_default()

'''
try:
    cur.execute("INSERT INTO items VALUES (85522, 'PC FF Chicken Cutlets', 'PC Free From', 17.62)")
except:
    print("This item ID already exists. Please change it.\n")
'''

'''
for row in cur.execute("SELECT * FROM items"):
    print(row)
'''




readItems("chicken")

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