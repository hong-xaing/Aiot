import pyautogui
import time

# 564,-478    #英雄試煉
    # 555,-565    #章節11
    # 715,-599    #中間選項    
    # 1143,-309   #掃盪
    # 705,-265    #消除視窗
    # 495,-252    #點兩次確認
    # 705,-265    #消除視窗
    # 1185,-797   #X鍵
    # 1300,-816   #返回鍵
# # 添加延迟
def delay(seconds):
    time.sleep(seconds)

time.sleep(3)  
# 模拟左键点击操作
x, y = 976, -512  # 指定坐标位置戰役
pyautogui.click(x, y,clicks=2)
time.sleep(5)  
x, y = 564,-478    #英雄試煉
pyautogui.click(x, y,clicks=1)
delay(5)  
x, y = 495,-612    #章節18
pyautogui.click(x, y,clicks=1)
delay(5)  
x, y = 715,-599    #中間選項 
pyautogui.click(x, y,clicks=1)
delay(4)  
click_count = 0
while True:
    if click_count < 1 :
        x, y = 1143,-309   #掃盪
        pyautogui.click(x, y,clicks=1)
        delay(4)  
        x, y = 705,-265    #消除視窗
        pyautogui.click(x, y,clicks=1)
        delay(4)  
        x, y = 495,-252    #點兩次確認 
        pyautogui.click(x, y,clicks=1)
        delay(4)  
        x, y = 495,-252    #點兩次確認 
        pyautogui.click(x, y,clicks=1)
        delay(4)  
        x, y = 705,-265    #消除視窗
        pyautogui.click(x, y,clicks=1)
        delay(4)  
        x, y = 705,-265    #消除視窗
        pyautogui.click(x, y,clicks=1)
        click_count += 1
    else :
        delay(4)  
        x, y = 1185,-797   #X鍵
        pyautogui.click(x, y,clicks=1)
        delay(4)  
        x, y = 1300,-816   #返回鍵
        pyautogui.click(x, y,clicks=1)
        break

# 564 -478    英雄試煉
# 905 -478    西域遠征
# 1178 -478   傳說之戰
# 1305 -478   往右邊
# 1300 -816   返回鍵