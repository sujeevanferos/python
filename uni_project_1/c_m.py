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
            print("PLEASE WAIT FOR A WHILE...")
            time.sleep(5)
            print("here is your ",selection," ... and here is your change: ",change)
            resources["water"] -= s_coffee["water"]
            resources["milk"] -= s_coffee["milk"]
            resources["coffee"] -= s_coffee["coffee"]
            resources["money"] += income

    elif selection == "off":
        username = input("\n USERNAME \n")
        password = askpass("\n PASSWORD \n")
        if username == "user" and password == "0000":
            time.sleep(3)
            break
        else:
            print(" INVALID USERNAME OR PASSWORD !!!")
    elif selection == "report":
        username = input("\n USERNAME \n")
        password = askpass("\n PASSWORD \n")
        if username == "user" and password == "0000":
            print("PLEASE WAIT!!!")
            time.sleep(1)
            print(resources)
        else:
            print(" INVALID USERNAME OR PASSWORD !!!")
    else:
        print(" - - I N V A L I D _ O P T I O N - - ")
    