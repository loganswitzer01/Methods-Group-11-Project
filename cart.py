import sqlite3
import sys
from tokenize import String


class cart:
    def _init_(self, user_id, cart_id, quantiy, book_name, book_id):
        self.user_id = user_id
        self.cart_id = user_id + 69
        self.quanity = 0
        self.book_name = []
        self.book_id = []

    #view the items in the cart
    def view(self):

        #tries to connect to the db
        try:
            connection = sqlite3.connect("methods.db")
        except:
            print("\nFailed connection\n")
            sys.exit()
            
        #will display the items in the cart once conned to db
        if self.quanity == 0:
            print("\nThe cart is empty\n")
        else:
            
            #connects the cursor to write to the table
            cursor = connection.currsor()
            cursor.execute("SELECT * FROM Cart")
            result = curcor.fetchall()

            #inputs in all the items into the db
            for x in self.book_name:
                print("Title:", x[1])

            #closes the cursor
            cursor.close()
            connection.close()

    #add item to the cart
    def add(self, bname, bid, number):
        bname = input("\n What book would you like to add: \n")
        number = 0

        #makes sure the user can not add a negative number
        while number == 0:
             number = input("How many would you like to add: \n")
             if number < 0:
                number = 0
            
    

        #tries to connect to the db
        try:
            connection = sqlite3.connect("methods.db")
        except:
            print("\nFailed connection\n")
            sys.exit()

        #adds items to the db
        while number != 0:
            self.book_name.append(bname)
            self.book_id.append(bid)
            self.quanity +=1
            number -=1
    	

    # need to look to see if it only remove one if there are duplicites
    def remove(self, bname, bid):
        bname = input("\n What book would you like to remove: \n")
        
        if bname in self.book_name:
            self.book_name.remove(bname)
            self.book_id.remove(bid)
            self.quanity -=1
        else:
            print("\nBook is not in cart\n")
            

    def edit(self, bname, bid, number):
        #adds to the cart based on number
        bname = input("\n Please enter the name of the book you would like to edit in quanity: \n")
        number = input("\n How nuch would you like to add or subtract:  \n")
        
        if number > 0:
            while number != 0:
                self.book_name.append(bname)
                self.book_id.append(bid)
                number -=1
                self.quanity +=1
        #removes form the cart based on number
        if number < 0:
            while number != 0:
                if bname in self.book_name:
                    self.book_name.remove(bname)
                    self.book_id.remove(bid)
                    self.quanity -=1
                    number +=1
                else:
                    print("\n No more books of that name are left in the cart!\n")
                    number = 0
                

    def checkOut(cart):

    def decreaseStock(cart):

    def clear(self):
        self.book_name.clear()
        self.book_id.clear()

        
