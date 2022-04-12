import pyautogui as pg
import time

print("Program will rn in5 sec")
time.sleep(5)
for i in range(2):
    pg.write("Hi")
    time.sleep(0.5)
    pg.press("Enter")