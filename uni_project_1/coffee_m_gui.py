from coffee_machine import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both",expand=True)

label = customtkinter.CTkLabel(master=frame, text="Coffee Machine")
label.pack(pady=12, padx=10)

button1 = customtkinter.CTkButton(master=frame, text="Espresso")
button1.pack(pady=12, padx=10)

button2 = customtkinter.CTkButton(master=frame, text="Cappuccino")
button2.pack(pady=12, padx=10)

button3 = customtkinter.CTkButton(master=frame, text="Latte")
button3.pack(pady=12, padx=10)

button4 = customtkinter.CTkButton(master=frame, text="Report", command = CoffeeMachine.run)
button4.pack(pady=12, padx=10)

button5 = customtkinter.CTkButton(master=frame, text="Power Off", command = root.destroy)
button5.pack(pady=12, padx=10)

root.mainloop()