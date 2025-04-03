from tkinter import Tk, Label
import time

class DigitalClock:
    def __init__(self, master):
        self.master = master
        master.title("Digital Clock")

        self.label = Label(master, font=("Helvetica", 48), bg="black", fg="white")
        self.label.pack()

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.label.config(text=current_time)
        self.master.after(1000, self.update_clock)

if __name__ == "__main__":
    root = Tk()
    clock = DigitalClock(root)
    root.mainloop()