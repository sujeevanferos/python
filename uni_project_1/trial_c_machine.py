
class Coffee_Machine1:
    ingredients = {
        "water" : 5000,
        "milk" : 5000,
        "coffee" : 1000,
        "cost" : 0
        }

    def main_menu():
        menu_choice = input("coffee, report, off :  ").lower()
        if menu_choice == "off":
            print("Shutting Down... ")
        elif menu_choice == "coffee":
            Coffee_Machine1.coffee_selection()
        elif menu_choice == "report":
            Coffee_Machine1.report()
        else:
            print("invalid keyword...!!!")
    
        
    def coffee_selection():
        drinks = {
        "espresso" : {"water" : 50, "milk" : 0, "coffee" : 18, "cost" : 1.5},
        "latte" : {"water" : 200, "milk" : 150, "coffee" : 24, "cost" : 2.5},
        "cappuccino" : {"water" : 200, "milk" : 100, "coffee" : 24, "cost" : 3.0}
        }
        coffee_choice = input("Espresso, Latte, Cappuccino : ").lower()
        if coffee_choice in drinks:
            selection = drinks[coffee_choice]

        else:
            print("invalid option .... ")

    def report():
        print(Coffee_Machine1.ingredients)





if __name__ == "__main__":
    Coffee_Machine1.main_menu()