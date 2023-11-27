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

            ## exits the program if unsuccessful
            sys.exit()

        print() ## spacing's sake

        ## cursor to send queries through
        cursor = connection.cursor()

        ## sends query and grabs data
        ## SELECT queries return a tuple for each row contained in a list
        ## --> a list of tuples
        cursor.execute("SELECT * FROM inventory")

        ## only needed if you're running a SELECT
        ## this actually grabs the data
        result = cursor.fetchall()

        ## illustrates what unformatted results look like
        print("Entire result set: ", result, sep="\n", end="\n\n\n")

        ## close the cursor and connection once you're done
        cursor.close()
        connection.close()

    def searchInventory(self):
        print("Here is the search")

    def decreaseStock(self, ISBN):
        print()