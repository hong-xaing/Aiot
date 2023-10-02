import pyautogui
import time
import keyboard  # 导入keyboard库

# 添加延迟函数
def delay(seconds):
    time.sleep(seconds)

# 监听键盘事件的回调函数
def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        if e.name == 'esc':  # 如果按下了ESC键
            print("ESC键被按下，程序停止")
            exit()

# 注册键盘事件监听器
keyboard.on_press(on_key_event)

# 开始执行程序

delay(4)
x, y = 976, -512  # 指定坐标位置戰役
pyautogui.click(x, y, clicks=2)
delay(4)
x, y = 261, -478  # 太平幻界
pyautogui.click(x, y, clicks=1)
delay(delay(4))
x, y = 1221, -414  # 更新
pyautogui.click(x, y, clicks=1)
delay(delay(4))
x, y = 900, -384  # 確認
pyautogui.click(x, y, clicks=1)
delay(delay(4))
x, y = 1221, -500  # 掃蕩
pyautogui.click(x, y, clicks=1)
delay(delay(4))
x, y = 1221, -600  # 畫面離開
pyautogui.click(x, y, clicks=1)
delay(delay(4))
x, y = 916, -215  # 精銳挑戰
pyautogui.click(x, y, clicks=1)
delay(delay(4))
x, y = 474, -264  # 精銳挑戰董卓可省略
pyautogui.click(x, y, clicks=1)
delay(delay(4))

click_count = 0
while True:
    if click_count < 10:
        x, y = 474, -264  # 精銳挑戰董卓可省略
        pyautogui.click(x, y, clicks=1)
        x, y = 665, -375  # 精銳掃蕩
        pyautogui.click(x, y)  # 模拟一次点击
        click_count += 1
        delay(1)
    else:
        # 执行下一个点击动作，这里可以添加适当的代码
        click_count = 0  # 重置点击次数
        delay(delay(4))
        x, y = 1185, -797  # X鍵
        pyautogui.click(x, y, clicks=1)
        delay(delay(4))
        x, y = 1300, -816  # 返回鍵
        pyautogui.click(x, y, clicks=1)
        break

# 让程序保持运行，以便监听ESC键
keyboard.wait('esc')
