import sqlite3 as sql
import sys

def login():
  while True:
    username = input("\nInput username: ")
    password = input("Input password: ")
    with sql.connect("users.db") as db:
      cursor = db.cursor()
    find_user = ("SELECT * FROM user WHERE uName = ? AND passWd = ?")
    cursor.execute(find_user, [(username), (password)])
    results = cursor.fetchall()

    if results:
      for r in results:
        print("\nWelcome", r[2])
      return("exit")
    else:
      print("Username or password not correct")
      again = input("Do you want to try again (y/n): ")
      if again.lower() == "n":
        return("exit")

def signup():
  while True:
    username = input("\nPlease input a username: ")
    with sql.connect("users.db") as db:
      cursor = db.cursor()
    find_user = ("SELECT * FROM user WHERE uName = ?")
    cursor.execute(find_user, [(username)])

    if cursor.fetchall():
      print("\nUsername taken...")
    else:
      break

  fname = input("Please input your first name: ")
  lname = input("Please input your last name: ")
  passwd = input("Please enter a password: ")
  passwd1 = input("Please re-enter your password: ")
  while passwd != passwd1:
    print("Passwords did not match, please try again")
    passwd = input("Please enter a password: ")
    passwd1 = input("Please re-enter your password: ")
  insert_data = '''INSERT INTO user(uName, fName, lName, passWd)
  VALUES(?,?,?,?)'''
  cursor.execute(insert_data, [(username),(fname),(lname),(passwd)])
  db.commit()

def menu():
  while True:
    print("Welcome, you whore")
    menu = ('''
    1. Create new user
    2. Login to system
    3. Exit\n''')

    choice = input(menu)

    if choice == "1":
      signup()
    elif choice == "2":
      login()
    elif choice == "3":
      print("Thank you, come again")
      sys.exit()
    else:
      print("Command not recognized")

menu()
