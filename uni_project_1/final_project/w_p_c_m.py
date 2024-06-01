import time, sys, os, datetime
from maskpass import askpass
from prettytable import PrettyTable
MENU = {
    "espresso":
        {
            "water": 50,
            "milk" : 0,
            "coffee": 18,
            "cost": 1.5
    },
    "latte": {
        
            "water": 200,
            "milk": 150,
            "coffee": 24,
            "cost": 2.5
    },
    "cappuccino": {
        
            "water": 250,
            "milk": 100,
            "coffee": 24,
            "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0
}

j = 1

while j >= 1:
    print(" _____________________________")
    print(" - - - - W E L C O M E - - - - ")
    print(" _____________________________")
    time.sleep(0.5)
    print("\n        --MENU--   \n")
    time.sleep(0.1)
    print("_COFFEE ITEM_      _PRICE_")
    time.sleep(0.1)
    print(" Espresso           $1.5 ")
    time.sleep(0.1)
    print(" Latte              $2.5 ")
    time.sleep(0.1)
    print(" Cappuccino         $3.0 ")
    time.sleep(0.5)
    selection = input("\n PLEASE SELECT YOUR COFFEE .... (espresso/latte/cappuccino) | 'off' for shut down | 'report' for view current resources  \n")
    if selection in MENU:

        s_coffee = MENU[selection]
        quantity = int(input("\n QUANTITY :\n"))
        
        if resources["water"] < quantity*s_coffee["water"] or resources["milk"] < quantity*s_coffee["milk"] or resources["coffee"] < quantity*s_coffee["coffee"]:
            print(" INSUFFICIENT INGREDIENTS !!! | SORRY FOR THE INCONVINIENCE ")
            time.sleep(2)
            os.system('cls')
        else:
            print(" This will cost $",quantity*s_coffee["cost"],"for your item ")
            
            money = int(input("\n--PLEASE INPUT MONEY--\n"))
            
            if money < quantity*s_coffee["cost"]:
                print("\n INSUFFICIENT MONEY \n")
                print("Your money $",money,"has successfully refunded")
                time.sleep(2)
                break
            else:
                change = money - quantity*s_coffee["cost"]
                income = money - change

            def progress_bar(total, current, bar_length=50):
                progress = current / total
                arrow = '#' * int(progress * bar_length)
                spaces = ' ' * (bar_length - len(arrow))
                sys.stdout.write('\rYOUR COFFEE IS BEING PREPARED: [{0}] {1:.2f}%'.format(arrow + spaces, progress * 100))
                sys.stdout.flush()

            total_items = 100
            for i in range(total_items):
                time.sleep(0.1)
                progress_bar(total_items, i + 1)

            time.sleep(1)
            print()
            print("\nHere is your ",selection)
            print()
            print("--------------------------------------------------")
            print("\n           - -  R E C E I E P T - -       \n")

            receipt = PrettyTable()
            columns = ["Coffee Item", "Quantity", " Total_Amount ($)"]
            receipt.add_column(columns[0], [selection])
            receipt.add_column(columns[1], [quantity])
            receipt.add_column(columns[2], [quantity*s_coffee["cost"]])
            print(receipt)
            print("Balance Amount : $",change)
            now = datetime.datetime.now()
            print("printed time : ",now.strftime("%y-%m-%d %H:%M:%S "))
            print("\n--------------------------------------------------\n")
            print()
            
            resources["water"] -= quantity*s_coffee["water"]
            resources["milk"] -= quantity*s_coffee["milk"]
            resources["coffee"] -= quantity*s_coffee["coffee"]
            resources["money"] += income
            time.sleep(2)
            a = input("\n Do you want to make another order ? (y/n) : ")
            if a == "y":
                os.system('cls')
            elif a == "n":
                break
            else:
                print("invalid option")

    elif selection == "off":
        break

    elif selection == "report":

        username = input("\n USERNAME \n")
        password = askpass("\n PASSWORD \n")

        if username == "user" and password == "0000":
            print("PLEASE WAIT!!!")
            time.sleep(0.5)
            print()
            print(" WATER  : ",resources["water"])
            print(" MILK   : ",resources["milk"])
            print(" COFFEE : ",resources["coffee"])
            print(" CASH BALANCE  : $",resources["money"])
            x = input("enter 'm' to main menu : ")
            if x == "m":
                os.system('cls')
        else:
            print(" INVALID USERNAME OR PASSWORD !!! ")
            break
    else:
        print(" - - I N V A L I D _ O P T I O N - - ")
        time.sleep(0.5)
        os.system('cls')
    