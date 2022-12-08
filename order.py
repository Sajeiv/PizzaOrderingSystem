# CS 1026 Assignment 2 by Sajeiv Ravichandran

# The python file containing the generateReceipt(pizzaOrder) function is imported into this python file
from pizzaReceipt import *

# Variables are declared here as well as the tuple containing the list of toppings used for pizzas later on
TOPPINGS = ("ONION", "TOMATO", "GREEN PEPPER", "MUSHROOM", "OLIVE", "SPINACH", "BROCCOLI", "PINEAPPLE", "HOT PEPPER", "PEPPERONI", "HAM", "BACON", "GROUND BEEF", "CHICKEN", "SAUSAGE")
pizzaOrder = []
chosenSize = ""
chosenToppings = []
pizzaSize = ""

# The user is asked to input whether they want to order a pizza.
initiateOrder = input("Do you want to order a pizza?")

# If the user types in a blank string, it forces generateReceipt(pizzaOrder) function to proceed, which then tells the user that they did not order anything
if initiateOrder == "":
    generateReceipt(pizzaOrder)

# If the user types in any form of No or Q, it forces generateReceipt(pizzaOrder) function to run with a blank order
elif initiateOrder.upper() == "Q" or initiateOrder.upper() == "NO":
    generateReceipt(pizzaOrder)

# If a valid input was used, the user will then be prompted to decide on a pizza size between S,M,L, or XL
else:
    # While a proper size is not inputed, the program will keep asking the user to input a valid size
    while pizzaSize.upper() != "S" and pizzaSize.upper() != "M" and pizzaSize.upper() != "L" and pizzaSize.upper() != "XL":
        pizzaSize = input("Choose a size: S,M,L,XL: ")

    # The chosen size will be appended to the tuple that represents the current pizza thats being made
    chosenSize = pizzaSize.upper()
    pizzaX = (chosenSize, chosenToppings)

    # User is then asked to input toppings for the pizza they want
    pizzaToppings = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"\n('")

    # While the toppings input is not "X" which discontinues the toppings selection, it will ask the user to either type LIST for the menu or add toppings
    while pizzaToppings.upper() != "X":
        if pizzaToppings.upper() == "LIST":
            print(TOPPINGS)
            pizzaToppings = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"")

        # If the toppings input matches the TOPPINGS tuple, it will add the topping onto the current pizza tuple
        # If the chosen topping is already added to the pizza, the user will be prompted to add toppings without adding the duplicate
        elif pizzaToppings.upper() in TOPPINGS:
            if pizzaToppings.upper() not in chosenToppings:
                chosenToppings.append(pizzaToppings.upper())
                print("Added " + str(pizzaToppings.upper()) + " to your pizza")
                pizzaToppings = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"")
            else:
                pizzaToppings = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"")
        # If the user inputs a wrong spelling for the topping or even a different word overall, it will prompt the user to input toppings again
        else:
            print("Invalid topping")
            pizzaToppings = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"")

    # As soon as the user inputs X, the pizza is assumed to be finished and the tuple that represents the current pizza will be added/appended onto the list that represents the pizzaOrder parameter
    pizzaOrder.append(pizzaX)

    # When the user types X during the toppings prompt, it will ask the user if they want to continue ordering
    if pizzaToppings == "X" or pizzaToppings == "x":
        continueOrder = input("Do you want to continue ordering?")

    # If the answer to this is Q or NO, it will generate a receipt with the pizza(s) that were made
    if continueOrder.upper() == "Q" or continueOrder.upper() == "NO":
        generateReceipt(pizzaOrder)

    # If the user types anything other than no or q, it will prompt the user to go through the process again and make a new pizza
    else:
        while continueOrder.upper() != "NO" and continueOrder.upper() != "Q":
            chosenSize = ""
            chosenToppings = []

            pizzaSize = input("Choose a size: S,M,L,XL: ")

            while pizzaSize.upper() != "S" and pizzaSize.upper() != "M" and pizzaSize.upper() != "L" and pizzaSize.upper() != "XL":
                pizzaSize = input("Choose a size: S,M,L,XL: ")

            chosenSize = pizzaSize.upper()
            pizzaX = (chosenSize, chosenToppings)

            pizzaToppings = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"")

            while pizzaToppings.upper() != "X":
                if pizzaToppings.upper() == "LIST":
                    print(TOPPINGS)
                    pizzaToppings = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"")

                elif pizzaToppings.upper() in TOPPINGS:
                    if pizzaToppings.upper() not in chosenToppings:
                        chosenToppings.append(pizzaToppings.upper())
                        print("Added " + str(pizzaToppings.upper()) + " to your pizza")
                        pizzaToppings = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"")
                    else:
                        pizzaToppings = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"")

                else:
                    print("Invalid topping")
                    pizzaToppings = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"")

            pizzaOrder.append(pizzaX)
            print(pizzaOrder)

            if pizzaToppings == "X" or pizzaToppings == "x":
                continueOrder = input("Do you want to continue ordering?")

        # When the user is done making pizzas, the program will go through and generate a receipt using the generateReceipt(pizzaOrder) function
        else:
            generateReceipt(pizzaOrder)
























