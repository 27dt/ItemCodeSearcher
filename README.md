DECEMBER 2023
Outside of school, I work part time in the meat department at a grocery store. 
One of my responsibilities is to be able to price items, which often come without a label. 
My job is to input the item's specific inventory code, and then weigh it on the scale, 
which assigns a price to it that corresponds to its code (example: inputting 85522 on the scale 
sets up the scale for us to be able to weigh and price chicken cutlets, which always comes unpriced 
from the factory). With all the products we carry, there is an extensive and ever-growing list 
printed out in the back room of the employee area. This list is now over 80 items long, and 
although I have memorized most of the codes I need, I know many others have not.

DECEMBER 2023:
There are two problems I intend to solve with my code: for starters, I want to create a program 
that allows a user to search through a list of all the code/item combinations. To do this, I 
must digitize the paper list into a text file, and allow the user to enter a search query (chicken, beef,
ham, etc), to which the program will output all results that match the input value. Second, I want to give the 
user the ability to add a new item to the list. This will be done by retrieving values for the scale 
code - and the product name - from the user, and writing it to the end of the existing text file. 
This way, the new item becomes a part of the existing list, and the user now has the ability to search for it.

---------------------------------------------------------------------------------------------------------------

AUGUST 2024:
I have uploaded this project to Github for easier developing, as I intend on overhauling it:

1) Add DB functionality with SQLite3 to create a table of items
    (Note that this will replace .txt file reading functionality)
    - This allows for easier item creation and getting
    - This introduces the ability to easily update and delete items
        - CRUD!
    - Apart from code and name, product category and weight price are added


2) Use TKinter to go from a text interface to a GUI
    - This allows for an easier-to-use program
    - This allows me to overhaul the interface of the program (button creation, etc.)