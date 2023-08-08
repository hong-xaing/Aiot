import serial
import modbus_tk
from modbus_tk import modbus_rtu
import modbus_tk.defines as cst

# 讀取
PORT = "COM1"

master = modbus_rtu.RtuMaster(serial.Serial(port=PORT,baudrate=9600,bytesize=8,parity="N",stopbits=1))
master.set_timeout(3.0)
master.set_verbose(True)  #怕被干擾，是否重發

value = master.execute(1,cst.READ_HOLDING_REGISTERS,0x100C,1)

print(value)

master.close