
'''
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