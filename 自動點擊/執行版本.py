import pyautogui
import time

# 251 -478   太平幻界
    # 1221,-414   更新
    # 900,-384  確認
    # 1221,-500   掃蕩
    # 1221,-600 # 畫面離開 
    # 916,-215   精銳挑戰
    # 474,-264   董卓
    # 665,-375   精銳掃蕩
    # 1185,-797    X鍵
    # 1300,-816    返回鍵
# # 添加延迟

def delay(seconds):
    time.sleep(seconds)

time.sleep(3)  
# 模拟左键点击操作
x, y = 976, -512  # 指定坐标位置戰役
pyautogui.click(x, y,clicks=2)
time.sleep(3)  
x, y = 261, -478 #太平幻界
pyautogui.click(x, y,clicks=1)
delay(4)  
x, y = 1221,-414 # 更新
pyautogui.click(x, y,clicks=1)
delay(4)  
x, y = 900,-384  # 確認
pyautogui.click(x, y,clicks=1)
delay(4)  
x, y = 1221,-500 # 掃蕩 
pyautogui.click(x, y,clicks=1)
delay(4)  
x, y = 1221,-600 # 畫面離開 
pyautogui.click(x, y,clicks=1)
delay(4)  
x, y = 916,-215 # 精銳挑戰 
pyautogui.click(x, y,clicks=1)
delay(4)  
x, y = 474,-264 # 精銳挑戰董卓可省略
pyautogui.click(x, y,clicks=1)
delay(4)  

click_count = 0
while True:
    if click_count < 10:
        x, y = 474,-264 # 精銳挑戰董卓可省略
        pyautogui.click(x, y,clicks=1)
        x, y = 665,-375 # 精銳掃蕩 
        pyautogui.click(x, y)  # 模拟一次点击
        click_count += 1
        time.sleep(1)
    else:
        # 执行下一个点击动作，这里可以添加适当的代码
        click_count = 0  # 重置点击次数
        delay(4)  
        x, y = 1185,-797 # X鍵
        pyautogui.click(x, y,clicks=1)
        delay(4)  
        x, y = 1300,-816 # 返回鍵
        pyautogui.click(x, y,clicks=1)
        break
# 564 -478    英雄試煉
# 905 -478    西域遠征
# 1178 -478   傳說之戰
# 1305 -478   往右邊
# 1300 -816   返回鍵


# delay(4)  
# x, y = 1305,-478 # 更新
# pyautogui.click(x, y,clicks=2)

# # 密寶探索
# delay(4)  
# x, y = 1178,-478  # 密寶探索
# pyautogui.click(x, y,clicks=1)
# delay(4)  
# x, y = 900,-384  # 確認
# pyautogui.click(x, y,clicks=1)
# delay(4)  
# x, y = 1221,-500 # 掃蕩 
# pyautogui.click(x, y,clicks=1)
# delay(4)  
# x, y = 1221,-600 # 畫面離開 
# pyautogui.click(x, y,clicks=1)
# delay(4)  
# x, y = 916,-215 # 精銳挑戰 
# pyautogui.click(x, y,clicks=1)
# delay(4)  
# x, y = 474,-264 # 精銳挑戰董卓可省略
# pyautogui.click(x, y,clicks=1)
# delay(4)

# click_count = 0
# while True:
#     if click_count < 10:
#         x, y = 474,-264 # 精銳挑戰董卓可省略
#         pyautogui.click(x, y,clicks=1)
#         x, y = 665,-375 # 精銳掃蕩 
#         pyautogui.click(x, y)  # 模拟一次点击
#         click_count += 1
#         time.sleep(1)
#     else:
#         # 执行下一个点击动作，这里可以添加适当的代码
#         click_count = 0  # 重置点击次数
#         delay(4)  
#         x, y = 1185,-797 # X鍵
#         pyautogui.click(x, y,clicks=1)
#         delay(4)  
#         x, y = 1300,-816 # 返回鍵
#         pyautogui.click(x, y,clicks=1)
#         break