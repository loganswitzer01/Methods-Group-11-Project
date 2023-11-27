import sqlite3
import sys

class Inventory:  
    dbName = ""
    tableName = ""

    def Inventory(self):
        dbName = ""
        tableName = ""

    def Inventory(self, indbName, intableName):
        dbName = indbName
        tableName = intableName
    
    def viewInventory(self):
        ## attempts to connect to the database
        try:
            connection = sqlite3.connect("methods.db")

            print("Successful connection.")

        except:
            print("Failed connection.")

            sys.exit()

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM inventory")

        result = cursor.fetchall()

        for x in result:
        ## you can print the entire tuple --> print(x)
        ## or you can print items from it using indices
        ## first item --> x[0]
        ## second item --> x[1]
        ## etc... (for however many columns a result has)
            print("Title:", x[1]) ## only the ISBN
            print("\tAuthor:", x[2], "\tISBN:", x[0])
            print("\tGenre:", x[3], "\tRelease Date:", x[4])
            print("\tPages:", x[5], "\tNumber in Stock:", x[6], "\n")

        cursor.close()
        connection.close()

    def searchInventory(self):
        print("Here is the search")

    def decreaseStock(self, ISBN):
        print()