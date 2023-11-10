import sqlite3
class User:  
    dbName = ""
    tableName = ""
    loggedIn = false
    userID = ""
  
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
        print("userID: ", userID)

    def createAccount():

    def getLoggedIn(string inloggedIn):
        loggedIn = inloggedIn

    def getUserID(string inuserID):
        userID = inuserID

    
