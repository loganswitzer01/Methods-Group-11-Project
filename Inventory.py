import sqlite3
import sys
from tokenize import String

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
        try:
            connection = sqlite3.connect("methods.db")

        except:
            print("Failed connection.")

            sys.exit()

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Inventory")

        result = cursor.fetchall()

        for x in result:
            print("Title:", x[1])
            print("\tAuthor:", x[2], "\tISBN:", x[0])
            print("\tGenre:", x[3], "\tRelease Date:", x[4])
            print("\tPages:", x[5], "\tNumber in Stock:", x[6], "\n")

        cursor.close()
        connection.close()

    def searchInventory(self):
        title = input("\n Please enter a title here: ")
        inTitle = str(title)

        print("\nSearch Results:")

        try:
            connection = sqlite3.connect("methods.db")

        except:
            print("Failed connection.")

            sys.exit()

        cursor = connection.cursor()

        search="SELECT * FROM inventory WHERE Title LIKE \"%"+inTitle+"%\""

        cursor.execute(search)

        result = cursor.fetchall()

        for x in result:
            print(" Title:", x[1])
            print("\t Author:", x[2], "\tISBN:", x[0])
            print("\t Genre:", x[3], "\tRelease Date:", x[4])
            print("\t Pages:", x[5], "\tNumber in Stock:", x[6])

        cursor.close()
        connection.close()

    def decreaseStock(self, ISBN):
        print()