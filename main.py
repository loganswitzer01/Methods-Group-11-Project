import sqlite3

class main:
  print("Welcome to the Book Nook! \n (1) Login \n (2) Create Account \n (3) Logout")

  preLogin = input(" Please choose an option here: ")
  inPreLogin = int(preLogin)

  if(inPreLogin == 1):
      print("\nWelcome to the Book Nook!")
  elif(inPreLogin == 2):
      print("\nCreating Account")
  elif(inPreLogin == 3):
      print("\nYou have successfully Logged Out")
  else:
      print("Invalid Response...")

