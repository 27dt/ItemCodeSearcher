import sys
import sqlite3


from default.load_default import *

conn = sqlite3.connect('db/items.db')
cur = conn.cursor()

#rebuild_table()
#reload_default()

conn.commit()

for row in cur.execute("SELECT * FROM items"):
    print(row)

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

def createItems(item_id, item_name, item_cat, item_price):
    pass
'''

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



'''
readItems("chicken")
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