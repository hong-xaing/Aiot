# 變數1 輸入小時 , 變數2 : 輸入1 的時候 1 hr = 60 min , 輸入2  1hr = 70 min
# hr = int(input("please enter A number : "))
# location = input("please enter B number : ")
# def hour(hr,location):
#     if location == "1":
#         location = 60
#         c = hr * location
#         print(str(c)+"min")
#     elif location == "2":
#         location = 70
#         c = hr * location
#         print(str(c)+"min")
#     else:
#         print("error")
# hour(hr,location)
# a = int(input("請輸入A"))
# b = int(input("請輸入B"))
# choose = input("請輸入1 OR 2")
# def calculate(a,b,choose):
#     if choose == "1":
#         c = a+b
#         print(c)
#         return c

#     elif choose == "2":
#         d = a-b
#         print(d)
#         return d

# result = calculate(a,b,choose) 
# print (result)


class Email:
    def set_address(self,address):
        print(address)
    def set_name(firstName,lastName):
        print("你的名字:"+firstName)

        print("你的姓氏:"+lastName)
toTaichungMail = Email()
toTaichungMail.set_address("台中市西屯區")
youname = Email()
# firstName =input("請輸入你的名字 : ")
# lastName = input("請輸入你的姓氏 : ")
# youname.set_name(firstName,lastName)
youname.set_name("鴻祥","呂")
