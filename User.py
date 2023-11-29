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
  
    def User():
        loggedIn = false
        userID = ""
        
    def User(string indbname, string intableName):
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
        print("User ID: ", userID)
        print("Email: ", email)
        print("Password: ", password)
        print("First Name: ", firstName)
        print("Last Name: ", lastName)
        print("Address: ", address)
        print("City: ", city)
        print("State: ", state)
        print("Zip: ", zip)
        print("Payment: ", payment)

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

    
