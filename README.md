**ABOUT**
This originated as a first-year university project in December 2023.

Grocery stores frequently receive items that need to be priced, such as packages of meat.
These items are priced by entering their item code on a scale, and weighing them.
- Ex: Inputting '85522' on the scale may set the scale up to price chicken cutlets.
In the grocery store I work at, this list of item codes is an outdated piece of paper taped to a wall.

The ItemCodeSearcher app intends to solve the problem of an outdated and hard-to-search paper list.
Upon running the app, a user now has the following options:
- Creating a new item (entering an ID, name, category, and price)
- Deleting an item
- Reading an item (entering an ID and having its corresponding item returned)
- Updating an existing item's name, category, and price
- Search for a list of corresponding items by entering a name search query

Seconday functions include:
- The ability to rebuild the table and reload its default entries
- The ability to get a full list of all items in the table

The app has been created in **Python**, uses **SQLite3** to manage the database, and **TKinter** for UI. 

---------------------------------------------------------------------------------------------------------------

**ROADMAP: AUGUST 2024:**
I have uploaded this project to Github for easier developing, as I intend on overhauling it:

1) Add DB functionality with SQLite3 to create a table of items **DONE**
    (Note that this will replace .txt file reading functionality) 
    - This allows for easier item creation and getting
    - This introduces the ability to easily update and delete items
        - CRUD!
    - Apart from code and name, product category and weight price are added


2) Use TKinter to go from a text interface to a GUI
    - This allows for an easier-to-use program
    - This allows me to overhaul the interface of the program (button creation, etc.)

**ROADMAP: DECEBER 2024:**
1) Utilize Flask to turn the existing files into a backend (routes implementation)

2) Consider creating a front end to turn the project into a full-stack application

---------------------------------------------------------------------------------------------------------------

**QUICK START:**
To delete and reload the table, as well as reload the default entries, do the following:

```python

rebuild_table()
reload_default()

```
