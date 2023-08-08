import modbus_servo_fake as ms
import serial
import modbus_tk
from modbus_tk import modbus_rtu
import modbus_tk.defines as cst
# def servo_on():
#     print ("servo on")
# def servo_off():
#     print ("servo off")
def go_initial():
    print ("return to origin")
def user_move():
    # try:
    move = input ("請輸入你的位置:")
    print ("你現在的位置:"+float(move))
    # except:
    #     move = input ("請重新輸入你的位置：")
    #     print("你現在的位置:"+ move)
    
PORT = "COM1"
try:
    master = ms.initial()
    # master = modbus_rtu.RtuMaster(serial.Serial(port=PORT,baudrate=9600,bytesize=8,parity="N",stopbits=1))
    # master.set_timeout(3.0)
    # master.set_verbose(True)

    while True:

        userInput = input("請輸入1為伺服啟動,2為伺服關閉,3為原點賦歸,4為輸入移動位置,5為離開程式: ")
        if userInput == '1':
            ms.servo_on(master)
        elif userInput == '2':
            ms.servo_off(master)
        elif userInput == '3':
            go_initial()
        elif userInput == '4':
            user_move()
        elif userInput == '5':
            print("EXIT")
            master.close()
            break
        else:
            print("請重新輸入,1為伺服啟動,2為伺服關閉,3為原點賦歸,4為再輸入移動位置,5為離開程式: ")
except:
    print("error")  