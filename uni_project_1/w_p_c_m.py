import time
import sys
from maskpass import askpass
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

i = 1
print(" - - - - W E L C O M E - - - - ")
time.sleep(2)
while i >= 1:
    selection = input("\n PLEASE SELECT YOUR COFFEE .... (espresso/latte/cappuccino) | 'off' for shut down | 'report' for view current resources  \n")
    if selection in MENU:
        s_coffee = MENU[selection]
        print(" This will cost ",s_coffee["cost"],"for your item ")
        money = int(input("\n--PLEASE INPUT MONEY--\n"))
        if money < s_coffee["cost"] or resources["water"] < s_coffee["water"] or resources["milk"] < s_coffee["milk"] or resources["coffee"] < s_coffee["coffee"]:
            print("\n unable to make coffee and here is your money \n",money)
        else:
            change = money-s_coffee["cost"]
            income = money-change

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
            print("\nhere is your ",selection," and here is your change: ",change,"\n")
            time.sleep(1)
            resources["water"] -= s_coffee["water"]
            resources["milk"] -= s_coffee["milk"]
            resources["coffee"] -= s_coffee["coffee"]
            resources["money"] += income

    elif selection == "off":
        username = input("\n USERNAME \n")
        password = askpass("\n PASSWORD \n")
        if username == "user" and password == "0000":
            time.sleep(2)
            print(" SHUTTING DOWN ")
            time.sleep(1)
            break
        else:
            print(" INVALID USERNAME OR PASSWORD !!!")
    elif selection == "report":
        username = input("\n USERNAME \n")
        password = askpass("\n PASSWORD \n")
        if username == "user" and password == "0000":
            print("PLEASE WAIT!!!")
            time.sleep(1)
            print()
            print(" WATER  : ",resources["water"])
            print(" MILK   : ",resources["milk"])
            print(" COFFEE : ",resources["coffee"])
            print(" CASH BALANCE  : $",resources["money"])
        else:
            print(" INVALID USERNAME OR PASSWORD !!!")
    else:
        print(" - - I N V A L I D _ O P T I O N - - ")
    