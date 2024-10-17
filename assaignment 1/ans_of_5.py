import pyautogui
from time import sleep

a = int(input())
sleep(5)
for i in range(a+1):
    for j in range(0,i):
        pyautogui.write("#", interval= 0.25)
    pyautogui.write("\n")
pyautogui.click('enter')


