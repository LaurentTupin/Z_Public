# How to keep your computer active so your boss does not notice you are away

import time
import pyautogui
pyautogui.FAILSAFE = False

while True:
    time.sleep(10)
    # move mouse
    for i in range(10):
        o_pos = pyautogui.position()
        if o_pos.y > 1000:      pyautogui.moveTo(o_pos.x , 0)
        elif o_pos.x > 1000:    pyautogui.moveTo(0 , o_pos.y)
        else:                   pyautogui.moveTo(o_pos.x + 10, o_pos.y + 50)
        # print(o_pos.x, o_pos.y)
    # Press Shift
    pyautogui.press('shift')
    # print('------------------')
    
    