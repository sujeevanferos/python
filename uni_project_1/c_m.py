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

while i >= 1:
    selection = input("PLEASE SELECT YOUR COFFEE .... (espresso/latte/cappuccino) | 'off' for shut down | 'report' for view current resources  ")
    if selection in MENU:
        s_coffee = MENU[selection]
        print("This will cost ",s_coffee["cost"],"for your item")
        money = int(input("PLEASE INPUT MONEY "))
        if money < s_coffee["cost"] or resources["water"] < s_coffee["water"] or resources["milk"] < s_coffee["milk"] or resources["coffee"] < s_coffee["coffee"]:
            print("unable to make coffee and here is your money",money)
        else:
            change = money-s_coffee["cost"]
            income = money-change
            print("here is your ",selection," ... and here is your change",change)
            resources["water"] -= s_coffee["water"]
            resources["milk"] -= s_coffee["milk"]
            resources["coffee"] -= s_coffee["coffee"]

    elif selection == "off":
        exit()
    elif selection == "report":
        print(resources)
    else:
        print("unidentified keyword!!!")
    resources["money"] += income
    