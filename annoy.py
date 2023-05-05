import random
import pyautogui as pg
import time

animal = ('tada','tadadada','tadatadatada')          #You can type any message between the quotes to spam
time.sleep(8)

for i in range(500):                                 # set your desired range i.e. the number of time you want it to press enter.
    a=random.choice(animal)
    pg.write(a)
    pg.press('enter')

