import sqlite3
from Inventory import Inventory
from User import user
from cart import cart

class main:
    inv = Inventory()

    ## Login Page
    inPreLogin=0
    while(inPreLogin != 3):
        print("Welcome to the Book Nook! \n (1) Login \n (2) Create Account \n (3) Logout")
        preLogin = input(" Please choose an option here: ")
        inPreLogin = int(preLogin)

        ## Main Menu
        if(inPreLogin == 1):
            inMainMenu = 0
            while(inMainMenu != 1):
                print("\nWelcome to the Book Nook! \n (1) Logout \n (2) View Account Information \n (3) Inventory Information \n (4) Cart Information")
                mainMenu = input(" Please choose an option here: ")
                inMainMenu = int(mainMenu)
                
                ## Logout
                if(inMainMenu == 1):
                    print("\nLogged Out")
                
                ## View Account Info Page
                elif(inMainMenu == 2):
                    print("\nAccount Info")

                ## View Inventory Page    
                elif(inMainMenu == 3):
                    inInventory = 0
                    while(inInventory != 1):
                        print("\nInventory \n (1) Go Back \n (2) View Inventory \n (3) Search Inventory")
                        inventory = input(" Please choose an option here: ")
                        inInventory = int(inventory)
                        if(inInventory == 1):
                            print("Going Back...")
                        elif(inInventory == 2):
                            inv.viewInventory()
                        elif(inInventory == 3):
                            inv.searchInventory() 
                        else:
                            print("Invalid Response")
                
                ## View Cart Information Page
                elif(inMainMenu == 4):
                    inCart = 0
                    while(inCart != 1):
                        print("\nCart \n (1) Go Back \n (2) View Cart \n (3) Add Items to Cart \n (4) Remove an Item from Cart \n (5) Check Out")
                        cart = input(" Please choose an option here: ")
                        inCart = int(cart)
                        if(inCart == 1):
                            print("Going Back...")
                        elif(inCart == 2):
                            print("Viewing Cart...")
                        elif(inCart == 3):
                            print("Adding an item...")
                        elif(inCart == 4):
                            print("Removing an item...")
                        elif(inCart == 5):
                            print("Checking out...")
                        else:
                            print("Invalid Response")
                else:
                    print("Invalid")

        ## Create an Account Page
        elif(inPreLogin == 2):
            print("\nCreating Account")

        ## Logout    
        elif(inPreLogin == 3):
            print("\nYou have successfully Logged Out")
        else:
            print("Invalid Response...")
    
