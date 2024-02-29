class CoffeeMachine:
    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.money = 0

    def report(self):
        print(f"Water: {self.water}ml\nMilk: {self.milk}ml\nCoffee: {self.coffee}g\nMoney: ${self.money}")

    def check_resources(self, drink):
        return (
            self.water >= drink["water"]
            and self.milk >= drink["milk"]
            and self.coffee >= drink["coffee"]
        )

    def process_coins(self):
        print("Please insert coins.")
        quarters = int(input("Quarters: ")) * 0.25
        dimes = int(input("Dimes: ")) * 0.1
        nickels = int(input("Nickels: ")) * 0.05
        pennies = int(input("Pennies: ")) * 0.01
        total_money = quarters + dimes + nickels + pennies
        return total_money

    def make_coffee(self, drink):
        self.water -= drink["water"]
        self.milk -= drink["milk"]
        self.coffee -= drink["coffee"]
        self.money += drink["cost"]
        print(f"Here is your {drink['name']}. Enjoy!")

    def run(self):
        drinks = {
            "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5, "name": "espresso"},
            "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5, "name": "latte"},
            "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0, "name": "cappuccino"},
        }

        while True:
            user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

            if user_choice == "off":
                print("Coffee machine is turning off.")
                break
            elif user_choice == "report":
                self.report()
            elif user_choice in drinks:
                selected_drink = drinks[user_choice]

                if not self.check_resources(selected_drink):
                    print(f"Sorry, not enough resources to make {user_choice}.")
                else:
                    total_money = self.process_coins()

                    if total_money < selected_drink["cost"]:
                        print("Sorry, that's not enough money. Money refunded.")
                    else:
                        change = round(total_money - selected_drink["cost"], 2)
                        if change > 0:
                            print(f"Here is ${change} in change.")
                        self.make_coffee(selected_drink)
            else:
                print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    coffee_machine.run()
