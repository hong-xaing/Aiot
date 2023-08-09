# 機械控制 參考TC100
import serial
import modbus_tk
from modbus_tk import modbus_rtu
import modbus_tk.defines as cst
# pip3 install modbus_tk
# pip3 install pyserial
PORT = "COM1"

def servo_on():
    try:
        master = modbus_rtu.RtuMaster(serial.Serial(port=PORT,baudrate=9600,bytesize=8,parity="N",stopbits=1))
        master.set_timeout(3.0)
        master.set_verbose(True)  #怕被干擾，是否重發
                        # servo Num ,寫入ＯＲ讀取,開始(16進位),要跑幾個,清單數字
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0x2042,1,[1])    #寫入
        value = master.execute(3,cst.READ_HOLDING_REGISTERS,0x100C,1)      #讀取
        print (value)
        master.close()
    except:
        print("error")
def servo_off():
    try:
        master = modbus_rtu.RtuMaster(serial.Serial(port=PORT,baudrate=9600,bytesize=8,parity="N",stopbits=1))
        master.set_timeout(3.0)
        master.set_verbose(True)  #怕被干擾，是否重發
                        # servo Num ,寫入ＯＲ讀取,開始(16進位),要跑幾個,清單數字
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0x2042,1,[1])    #寫入
        value = master.execute(3,cst.READ_HOLDING_REGISTERS,0x100C,0)      #讀取
        print (value)
        master.close()
    except:
        print("error")
