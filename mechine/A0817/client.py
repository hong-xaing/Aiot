# import socket
# # print("HELLODOGSHIT")
# # ip = "120.109.128.30"
# ip = "127.0.0.1"
# port = 2234
# # port = 50

# # 連線的相關, 我用TCP/IP連線
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # tuple格式
# x = (ip,port)
# s.connect( x )


# while True:
# # 變成010101的格式送出去給其他電腦
#     data = input("請輸入")
#     s.send(data.encode())
#     if data == "-1":
#         print("自行斷掉")
#         break
#     getData = s.recv(1024)
#     finalData = getData.decode()
#     print(finalData)
#     if finalData == "-1":
#         print("收到斷掉")
#         break
   
#     # 加密的動作
#     # print (getData.decode())

# s.close()


import socket

ip = "127.0.0.1"
port = 2234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
x =(ip,port)

s.connect( x )

while True:
    data = input("請輸入想說的話或想結束對話請輸入END: ")
    s.send(data.encode())
    if data == "END":
        print("一切都結束了,下次再會")
        break
    getData = s.recv(1024)
    endData = getData.decode()
    print(endData)
    if endData == "END":
        break
s.close()
