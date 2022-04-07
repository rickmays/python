# This python program was written for my Codecademy computer science
# pro career path course in the object oriented programming section.
# The requirement was to create a game using at least two classes.
# I chose to create a simple store game, which includes a Store class and a
# Customer class. The point of the game is to demonstrate creating objects,
# instances of objects, and handling interactions between instances.

# time is imported to use time.sleep to slow things down so the
# whole game doesn't finish in less than a second :)

import time

# os is imported to enable clearing of the console screen at the start
# of the game

import os

# The Store class holds the store name, the type of store, the store
# inventory (containing items and their price), a shopping basket
# where items on the customer's grocery list are placed, and the
# sales total for the store.

class Store:
  name = ""
  type_of_store = ""
  inventory = {}
  basket = []
  sales = 0.00

  # Store constructor

  def __init__(self, input_name, input_type_of_store, input_inventory, input_basket = [], input_sales = 0.00):
    self.name = input_name
    self.type_of_store = input_type_of_store
    self.inventory = input_inventory
    self.basket = input_basket
    self.sales = input_sales

  # Store __repr__ method describes the Store class when you print it.

  def __repr__(self):
    return "This is a {name} store, which is a {type} store.\nIts inventory includes: {inventory}\nThe store's total sales are ${sales:0.2f}".format(name = self.name, type = self.type_of_store, inventory = self.inventory, sales = self.sales)

  # The Store add_inventory method adds a new item with its price to 
  # the store's inventory if it doesn't already exist
  
  def add_inventory(self, new_item, price):
    if new_item not in self.inventory:
      self.inventory.update({new_item:price})
      print(new_item + " added to inventory.")
    else:
      print(new_item + " not added. It is already in the inventory.")
    separator()
  
  # The Store change_price method changes the price of
  # an existing item

  def change_price(self, item, new_price):
    if item in self.inventory:
      old_price = self.inventory.get(item)
      self.inventory[item] = new_price
      print("Price of " + item + " changed from $" + str(round(old_price, 2)) + " to $" + str(round(new_price, 2)))
    else:
      print(item + " not found in inventory.")
    separator()
  
  # The Store checkout method checks with the customer to make sure
  # they are ready to checkout and if so it adds up the prices for 
  # all of the items in their basket, let's the customer know. If 
  # the customer has enough money to pay for the groceries it
  # deducts the money from their balance

  def checkout(self, customer):
    sale = 0.00
    response = input("Hello, " + customer.name +  ". Are you ready to check out?\n")
    if response.upper() in ("YES", "Y"):
      separator()
      for item in self.basket:
        print(item + " @ $" + str(round(self.inventory.get(item), 2)))
        sale += self.inventory.get(item)
      # self.basket = []
      separator()
      print("That will be $" + str(round(sale, 2)) + ", please.")
      separator()
      if customer.money >= sale:
        self.sales += sale
        customer.money -= sale
        print("Thank you, " + customer.name + ". You have $" + str(round(customer.money, 2)) + " remaining.")
        separator()
        print("Have a wonderful day and come back to see us!")
      else:
        print("I'm sorry, " + customer.name + ", but you don't have enough money.")
    separator()

  def store_sales(self):
    print("Total sales for this store are: $" + str(round(self.sales, 2)))
    separator()

# The Customer class holds the customer's name, grocery list, and money.
# It gives the customer the ability to add to their grocery list, 
# add more money, and shop for groceries.

class Customer:
  name = ""
  grocery_list = []
  money = 0.00

  # Customer constructor
  
  def __init__(self, input_name, input_grocery_list, input_money):
    self.name = input_name
    self.grocery_list = input_grocery_list
    self.money = input_money

  # The Customer __repr__ method describes the Customer class when you print it.

  def __repr__(self):
      return "This is a customer named {name}. {name}'s grocery list includes\n{grocery_list}\n{name} has ${money:0.2f} available.".format(name = self.name, grocery_list = self.grocery_list, money = self.money)

  # The Customer shop method compares their grocery list to the store's
  # inventory and adds items that are found to the basket. It also
  # informs the customer of any items on their grocery list that were
  # not in the store's inventory at the time.

  def shop(self, store):
    items_not_found = []
    store.basket = []
    for item in self.grocery_list:
      if item in store.inventory:
        store.basket.append(item)
      else:
        items_not_found.append(item)
    print("These items were added to your basket:")
    for item in store.basket:
      print(item)
    if items_not_found:
      separator()
      print("The following items are currently not in stock, please check back later:")
      for item in items_not_found:
        print(item)
    separator()

  # The Customer add_money method adds money to the customer's money balance.

  def add_money(self, money):
    self.money += money
    print("You now have $" + str(self.money))
    separator()

  # The Customer add_to_grocery_list adds new items to the customer's grocery list.
  
  def add_to_grocery_list(self, new_item, store):
    self.grocery_list.append(new_item)
    print(new_item + " has been added to your grocery list.")
    if new_item in store.inventory:
        store.basket.append(new_item)
    else:
      print(new_item + " is not in stock at this time. Please check back later.")
    separator()

# Utility functions

# This utility function prints a blank line, line of dashes, and a 
# blank line to give some separation between each activity.
# It also uses time.sleep to slow down the action a bit.

def separator():
  print("\n" + "-"*72 + "\n")
  time.sleep(1)

# Clearing the Screen
os.system('clear')

# Let the store game begin!
separator()
print("Let the store game begin!")
separator()

# Instantiate a Store, giving it a name, a type of store, and its initial inventory.
heb_store = Store("H-E-B", "grocery", {"Laundry Detergent": 7.49, "Cat Litter": 7.29, "Pistachios": 3.49, "Paper Plates": 2.68, "Toilet Paper": 6.28, "Paper Towels": 5.98, "Milk": 3.48, "Butter": 2.29, "Eggs": 2.24, "Cat Food": 6.58, "Dog Food": 9.29, "Vitamins": 6.48, "Aspirin": 3.59, "Hamburger": 8.40, "Chicken": 6.50, "Ice Cream": 5.45, "Cheese": 5.35, "Apples": 3.29, "Oranges": 3.69, "Strawberries": 3.48, "Blueberries": 4.98, "Bread": 5.48, "Spaghetti Sauce": 2.49, "Spaghetti": 2.59, "Tomatoes": 1.00, "Rice": 3.68, "Beans": .95})
print(heb_store)
separator()

# Instantiate a Customer, giving it a name, a grocery list, and some money to buy it with.
rick = Customer("Rick", ["Laundry Detergent", "Cat Litter", "Paper Plates", "Milk", "Apples", "Bread", "Pickles"], 50.00)
print(rick)
separator()

# Add an item with its price to the store inventory
heb_store.add_inventory("Walnuts", 6.49)

# Change the price of an item in the store
heb_store.change_price("Chicken", 6.25)

# Shop for groceries
rick.shop(heb_store)

# Add money to customer
rick.add_money(10.00)

# Add item to grocery list
rick.add_to_grocery_list("Pistachios", heb_store)
rick.add_to_grocery_list("Batteries", heb_store)

# Time to checkout and pay
heb_store.checkout(rick)

# Check total sales for the store
heb_store.store_sales()

# Shop for groceries
rick.shop(heb_store)

# Time to checkout and pay
heb_store.checkout(rick)

# Check total sales for the store
heb_store.store_sales()

# Check store __repr__ again
print(heb_store)
separator()

# Check customer __repr__ again
print(rick)
separator()

# Instantiate a Store, giving it a name, a type of store, and its initial inventory.
lowes_store = Store("Lowes", "Home Improvement", {"Cordless Drill": 47.49, "Hacksaw": 14.29, "Screwdriver Set": 16.49, "Garden Hose": 12.68, "Cement": 6.28, "AC Filter": 8.98, "Door Lock": 23.48, "Deck Screws": 8.29, "Plywood": 24.24, "2 x 4": 4.58, "PVC Pipe": 4.29, "Drywall": 28.48, "Ceiling Fan": 43.59, "Lamp": 18.40, "Extension Cord": 6.50, "Hammer": 8.45, "House Key": 5.35, "Sand": 4.29, "Compost": 3.69, "Shovel": 15.48, "Lawn Mower": 224.98, "BBQ Grill": 99.48, "Insulation": 15.49, "Ladder": 79.59, "Paint": 31.00, "Paint Brush": 3.68, "Seeds": 1.95})
print(lowes_store)
separator()

# Instantiate a Customer, giving it a name, a grocery list, and some money to buy it with.
carolin = Customer("Carolin", ["Garden Hose", "Ladder", "AC Filter", "Lamp", "Ceiling Fan", "Paint", "Paint Brush", "Guitar"], 200.00)
print(carolin)
separator()

# Add an item with its price to the store inventory
lowes_store.add_inventory("Circular Saw", 76.49)

# Change the price of an item in the store
lowes_store.change_price("Hacksaw", 15.25)

# Shop for groceries
carolin.shop(lowes_store)

# Add money to customer
carolin.add_money(200.00)

# Add item to grocery list
carolin.add_to_grocery_list("Circular Saw", lowes_store)
carolin.add_to_grocery_list("Toothpaste", lowes_store)

# Time to checkout and pay
lowes_store.checkout(carolin)

# Check total sales for the store
lowes_store.store_sales()

# Shop for groceries
carolin.shop(lowes_store)

# Time to checkout and pay
lowes_store.checkout(carolin)

# Check total sales for the store
lowes_store.store_sales()

# Check store __repr__ again
print(lowes_store)
separator()

# Check customer __repr__ again
print(carolin)
separator()