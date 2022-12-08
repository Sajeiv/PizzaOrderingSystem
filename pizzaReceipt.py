# CS 1026 Assignment 2 by Sajeiv Ravichandran

# This python file is used to create the generateReceipt(pizzaOrder) which would be used in the order.py file
# The variables are declared at the top and will be used later for the function
def generateReceipt(pizzaOrder):
    tax = 1.13
    pizzaSize = ""
    pizzaSizePrice = 0.00
    totalPrice = 0.00
    finalTotal = 0.00
    finalTax = 0.00
    extraToppings = 0.00

    # If the pizzaOrder parameter that is received is blank, it will print and tell the user that they did not order anything
    if pizzaOrder == []:
        print("You did not order anything")
    # If the pizzaOrder parameter contains a pizza tuple, it will generate a proper receipt
    else:
        print("Your order: ")
        # This for loop counts the amount of elements in the pizzaOrder parameter, each element represents one pizza
        # This for loop is a good way to generate the necessary receipt details needed for each pizza one at a time
        for order in range(len(pizzaOrder)):

            # After counting the amount of pizzas, it will then count whether each pizza contains more than 3 toppings using the len function
            # Amount of extra toppings are recorded
            extraToppingsCounter = len(pizzaOrder[order][1]) - 3

        # Numerous if elif statements are used to classify whether the current pizza fits into the small,medium,large or extra large class

            # Small pizzas are recorded as S and have a starting price of 7.99
            if pizzaOrder[order][0] == "S":
                totalPrice = 7.99
                pizzaSizePrice = 7.99
                pizzaSize = "S"

                # If there are more than 3 toppings, each extra topping will be an extra 0.5 for this size
                if len(pizzaOrder[order][1]) > 3:
                    totalPrice = totalPrice + (len(pizzaOrder[order][1]) - 3)*0.5
                    extraToppings = 0.5

            # Medium pizzas are recorded as M and have a starting price of 9.99
            elif pizzaOrder[order][0] == "M":
                totalPrice = 9.99
                pizzaSizePrice = 9.99
                pizzaSize = "M"

                # If there are more than 3 toppings, each extra topping will be an extra 0.75 for this size
                if len(pizzaOrder[order][1]) > 3:
                    totalPrice = totalPrice + (len(pizzaOrder[order][1]) - 3)*0.75
                    extraToppings = 0.75

            # Large pizzas are recorded as L and have a starting price of 11.99
            elif pizzaOrder[order][0] == "L":
                totalPrice = 11.99
                pizzaSizePrice = 11.99
                pizzaSize = "L"

                # If there are more than 3 toppings, each extra topping will be an extra 1 for this size
                if len(pizzaOrder[order][1]) > 3:
                    totalPrice = totalPrice + (len(pizzaOrder[order][1]) - 3)*1
                    extraToppings = 1
            # If the current pizza arent the previous mentioned sizes they will be classified as extra large and start at 13.99
            else:
                totalPrice = 13.99
                pizzaSizePrice = 13.99
                pizzaSize = "XL"

                # If there are more than 3 toppings, each extra topping will be an extra 1.25 dollars
                if len(pizzaOrder[order][1]) > 3:
                    totalPrice = totalPrice + (len(pizzaOrder[order][1]) - 3)*1.25
                    extraToppings = 1.25

            # Within this for loop lies this statement at the end that adds the starting pizza price as well as the extra topping prices
            # Each time a new pizza's details and prices go through this huge for loop, it adds onto this final total
            finalTotal = finalTotal + totalPrice

            # finalTax is used to find what the tax was on the final price shown on the receipt
            # This is easily done by multiplying the final price by 0.13 then storing it into the finalTax variable
            finalTax = finalTotal * 0.13

            # This print statement shows the user the pizza number, size, and starting price of the pizza without toppings
            print("Pizza " + str(order+1) + ": " + pizzaSize + " 				   " + str(format(round(pizzaSizePrice, 2),".2f")))
            # This for loop is used to list out the toppings of the current pizza and print them
            for item in pizzaOrder[order][1]:
                print(f"- {item}")
            # While there are more than 3 toppings on the current pizza, it will print out the price of each extra topping on the current pizza
            while extraToppingsCounter > 0:
                extraToppingsCounter -= 1
                print("Extra Topping (" + pizzaSize + ")" + "          " + str(format(round(extraToppings, 2),".2f")))
        # The final two prints show the user the final price and tax at the end of the generated receipt
        print("Tax:" + "					   " + str(format(round(finalTax, 2), ".2f")))
        print("Total:" + "					  " + str(format(round(finalTotal*tax, 2), ".2f")))








