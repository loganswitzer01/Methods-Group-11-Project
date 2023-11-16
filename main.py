import sqlite3

class main:
  print("Welcome to the Book Nook! \n (1) Login \n (2) Create Account \n (3) Logout")

  preLogin = input(" Please choose an option here: ")
  inPreLogin = int(preLogin)

  if(inPreLogin == 1):
      print("\nWelcome to the Book Nook! \n (1) Logout \n (2) View Account Information \n (3) Inventory Information \n (4) Cart Information")
        mainMenu = input(" Please choose an option here: ")
        inMainMenu = int(mainMenu)
        if(inMainMenu == 1):
            print("\nLogged Out")
        elif(inMainMenu == 2):
            print("\nAccount Info")
        elif(inMainMenu == 3):
            print("\nInventory \n (1) Go Back \n (2) View Inventory \n (3) Search Inventory")
            inventory = input(" Please choose an option here: ")
            inInventory = int(inventory)
            if(inInventory == 1):
                print("Going Back...")
            elif(inInventory == 2):
                print("Inventory...")
            elif(inInventory == 3):
                print("Searching Inventory...")
            else:
                print("Invalid Response")
        elif(inMainMenu == 4):
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
  elif(inPreLogin == 2):
      print("\nCreating Account")
  elif(inPreLogin == 3):
      print("\nYou have successfully Logged Out")
  else:
      print("Invalid Response...")

