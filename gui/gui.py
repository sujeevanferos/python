import tkinter as tk

def greet():
    name = entry.get()
    if name:
        greeting.config(text=f"Hello, {name}!")
    else:
        greeting.config(text="Hello, there!")

# Create the main application window
root = tk.Tk()
root.title("Simple GUI")

# Create and pack widgets
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Greet", command=greet)
button.pack(pady=5)

greeting = tk.Label(root, text="")
greeting.pack(pady=10)

# Run the event loop
root.mainloop()
