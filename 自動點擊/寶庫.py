# 730 -267
import pyautogui
import time


click_count = 0
while True:
    if click_count < 20:
        x, y = 730,-267 # 
        pyautogui.click(x, y)
        time.sleep(7)
