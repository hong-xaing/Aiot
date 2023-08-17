# import socket

# # ip = "120.109.131.221"
# ip = "127.0.0.1"
# port = 2234
# maxConnextNumber = 5


# # 連線的相關, 我用TCP/IP連線
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# # bind跟connect綁定起來
# x = (ip,port)
# s.bind(x)
# s.listen(maxConnextNumber)


# con,addr = s.accept()
# print(addr)
# while True:
#     data = con.recv(1024)
#     print(data.decode())
#     if data.decode() == "-1":
#         break
#     else:
#         Inp = input("請輸入")
#         con.send(Inp.encode())
#         if Inp == "哭哇":
#             break

# con.close()


import socket

ip = "127.0.0.1"
port = 2234
maxConnectNumber = 5

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind((ip,port))
s.listen(maxConnectNumber)

user = []

con,addr = s.accept()
print(addr)


while True:    
    data = con.recv(1024)
    print(data.decode())
    if data.decode() == "END":
        break
    else:
        inPut = input("請輸入要傳送的話: ")
        con.send(inPut.encode())
        if inPut == "END":
            break
con.close()
