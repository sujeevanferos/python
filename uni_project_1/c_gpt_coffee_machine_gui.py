import tkinter as tk
from tkinter import messagebox

class CoffeeMachineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Machine")
        
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.money = 0
        
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="What would you like? (espresso/latte/cappuccino):")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.button = tk.Button(self.root, text="Submit", command=self.process_choice)
        self.button.pack()

        self.report_button = tk.Button(self.root, text="Report", command=self.generate_report)
        self.report_button.pack()

    def process_choice(self):
        choice = self.entry.get().lower()

        drinks = {
            "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5, "name": "espresso"},
            "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5, "name": "latte"},
            "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0, "name": "cappuccino"},
        }

        if choice == "off":
            self.root.quit()
        elif choice == "report":
            self.generate_report()
        elif choice in drinks:
            selected_drink = drinks[choice]

            if not self.check_resources(selected_drink):
                messagebox.showerror("Error", f"Sorry, not enough resources to make {choice}.")
            else:
                messagebox.showinfo("Payment", "Please insert coins.")
                total_money = self.process_coins()

                if total_money < selected_drink["cost"]:
                    messagebox.showerror("Error", "Sorry, that's not enough money. Money refunded.")
                else:
                    change = round(total_money - selected_drink["cost"], 2)
                    if change > 0:
                        messagebox.showinfo("Change", f"Here is ${change} in change.")
                    self.make_coffee(selected_drink)
        else:
            messagebox.showerror("Error", "Invalid choice. Please choose a valid option.")

    def generate_report(self):
        report = f"Water: {self.water}ml\nMilk: {self.milk}ml\nCoffee: {self.coffee}g\nMoney: ${self.money}"
        messagebox.showinfo("Report", report)

    def check_resources(self, drink):
        return (
            self.water >= drink["water"]
            and self.milk >= drink["milk"]
            and self.coffee >= drink["coffee"]
        )

    def process_coins(self):
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
        messagebox.showinfo("Enjoy!", f"Here is your {drink['name']}. Enjoy!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeMachineGUI(root)
    root.mainloop()
