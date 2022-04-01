from collections import OrderedDict
from bson.objectid import ObjectId
from pymongo import collection, mongo_client
from pymongo.mongo_client import MongoClient

from pprint import pprint

#from pymongo.read_preferences import make_read_preference

def menu():
    print("[1] Load")
    print("[2] View Customers")
    print("[3] View Products")
    print("[4] Place an order")
    print("[5] View Orders")
    print("[6] Create new customer")
    print("[7] Create new product")
    print("[8] Delete an order")
    print("[9] Update customer details")
    print("[0] Exit")

def insertcustomer():
    print("Create new customer")
    from pymongo import MongoClient
    client = MongoClient(port=27017)
    db = client.Project0
    
    collection = db.customers

    name = input("Enter your 'name': ")
    number = input("Enter your 'age': ")
    location = input("Enter your 'location': ")

    docu = {"name": (name), "age": (number), "Location": (location)}
    collection.insert_one(docu)
    print("New customer created!")

def loaddata():
    print()
    print("Data has been loaded!")
    from pymongo import MongoClient
    client = MongoClient(port=27017)
    db = client.Project0
    print("Orders list")
    collection = db.Orders

    for x in collection.find():
        pprint(x)
        print(" ")

    print(" ")
    print(" ")
    
    print("Customers list")
    collection = db.customers

    for x in collection.find():
        pprint(x)
        print(" ")

    print(" ")
    print(" ")

    print("Products list")
    collection = db.products   

    for x in collection.find():
        pprint(x)
        print(" ")

    print(" ")
    print(" ")


def deleteorder():
    print()
    from pymongo import MongoClient
    client = MongoClient(port=27017)
    db = client.Project0
    
    collection = db.Orders

    for x in collection.find():
        print(x)

    print(" ")
    print(" ")

    delvalue = str(input("Please enter the object id you wish to delete : "))
    collection.delete_one({"_id": ObjectId(delvalue)})
    print(delvalue + " Order has been deleted!")
    print(" ")

def viewcustomers():
    print()
    print("Customers have been loaded!")
    from pymongo import MongoClient
    client = MongoClient(port=27017)
    db = client.Project0

    collection = db.customers

    for x in collection.find():
        pprint(x)
        print(" ")

    print(" ")
    print(" ")

def updatecustomer():
    print()
    print("Customer has been updated!")
    from pymongo import MongoClient
    client = MongoClient(port=27017)
    db = client.Project0

    collection = db.customers

    #age = int(input("What is your current age?: "))
    #location = input("Where are you located?: ")
    name = input("What is your name?: ")

    #updated_age = int(input("What is your updated age?: "))
    #updated_location = input("Where have you moved to?: ")
    #updated_name = input("What is your updated name?: ")

    #try this method
    old_values = {"name" :name} 
    #{"location" :location}, {"age" :age})
    new_values = {"$set" :{"name" :"Kris Middletown"}}
    #{"location" :updated_location}, {"age" :updated_age})}
    collection.update_one(old_values, new_values)
    print("Hello")

    for x in collection.find():
        pprint(x)
        print(" ")

    print(" ")
    print(" ")

def viewproducts():
    print()
    print("Products have been loaded!")
    from pymongo import MongoClient
    client = MongoClient(port=27017)
    db = client.Project0

    collection = db.products

    for x in collection.find():
        pprint(x)
        print(" ")

    print(" ")
    print(" ")

def viewordersforcustomer():
    print()
    print("Orders have been loaded!")
    from pymongo import MongoClient
    client = MongoClient(port=27017)
    db = client.Project0

    collection = db.customers
    collection = db.Orders

    for x in collection.find():
        pprint(x)
        print(" ")

    print(" ")
    print(" ")

def placeorder():
    print()
    from pymongo import MongoClient
    client = MongoClient(port=27017)
    db = client.Project0
    
    collection = db.Orders

    orderid = input("Enter 'OrderID': ")
    item = input("Enter 'Item': ")
    quantity = input("Enter 'Quantity': ")
    total = input("Enter 'Total': ")

    docu = {"OrderID": (orderid), "Item": (item), "Quantity": (quantity), "Total": (total)}
    collection.insert_one(docu)
    print("Your order has been placed!")
    print()

    menu()    

def insertproduct():
    from pymongo import MongoClient
    client = MongoClient(port=27017)
    db = client.Project0
    
    collection = db.products

    item = input("Enter 'Item Name': ")
    price = input("Enter 'Price': ")
    description = input("Enter 'Description': ")

    docu = {"Item Name": (item), "Price": (price), "Description": (description)}
    collection.insert_one(docu)
    print("New Product created!")
    print()

menu()    
option = int(input("Select menu option: "))

while option != 0:
    if option == 1:
        loaddata()
    elif option == 2:
        viewcustomers()
    elif option == 3:
        viewproducts()
    elif option == 4:
        placeorder()
    elif option == 5:
        viewordersforcustomer()
    elif option == 6:
        insertcustomer()
    elif option == 7:
        insertproduct()
    elif option == 8:
        deleteorder()
    elif option == 9:
        updatecustomer()       
    else:
        option == 0
        print()
        print("Invalid option selected.")
    menu()
    option = int(input("Select menu option: "))

print("Thanks for using this program! Goodbye!")
 




