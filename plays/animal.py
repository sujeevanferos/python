import random,time
import pyautogui as pg 
animal = ('monkey','donkey','dog')
time.sleep(8)
for i in range(100):
    a=random.choice(animal)
    pg.write("punda")
    pg.press('enter')
