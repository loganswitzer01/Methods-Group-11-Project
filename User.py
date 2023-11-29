import sqlite3
import sys
from tokenize import String

class User:  
    dbName = ""
    tableName = ""
    loggedIn = false
    userID = ""
    email = ""
    password = ""
    firstName = ""
    lastName = ""
    address = ""
    city = ""
    state = ""
    zip = ""
    payment = ""
  
    def User(self):
        loggedIn = false
        userID = ""
        
    def User(self, string indbname, string intableName):
        dbName = indbName
        tableName = intableName
        loggedIn = false
        userID = ""
    
    def login(string inuserID):
        userID = inuserID
        loggedIn = true
        return true

    def logout():
        userID = ""
        loggedIn = false
        return false

    def viewAccountInformation():
        try:
                connection = sqlite3.connect("methods.db")
    
            except:
                print("Failed connection.")
    
                sys.exit()
    
            cursor = connection.cursor()
    
            cursor.execute("SELECT * FROM user")
    
            result = cursor.fetchall()
    
            for x in result:
                print("userID:", x[0])
                print("\tName:", x[3], x[4])
                print("\tEmail:", x[1], "\tPassword:", x[2])
                print("\tAdress:", x[5], x[6], x[7], x[8])
                print("\tPayment:", x[9])
    
            cursor.close()
            connection.close()

    def createAccount(string inuserID, string inemail, string inpassword. string infirstName, string inlastName, string inaddress, string incity, string instate, string inzip, string inpayment):
        userID = inuserID
        email = inemail
        password = inpassword
        firstName = infirstName
        lastName = inlastName
        address = inaddress
        city = incity
        state = instate
        zip = inzip
        payment = inpayment

    def getLoggedIn(string inloggedIn):
        loggedIn = inloggedIn

    def getUserID(string inuserID):
        userID = inuserID

    
