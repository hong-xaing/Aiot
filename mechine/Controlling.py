from Ver_TC100 import settingup,servoOn,servoOff,initial,designatedLocation,closeup

try:
    master=settingup()
    while True:
        choice=input("1.SERVO ON  2.SERVO OFF\n3.原點歸位  4.輸入位置  5.離開 -- ")
        if choice=="1":
            servoOn(master)
        elif choice=="2":
            servoOff(master)
        elif choice=="3":
            initial(master)
        elif choice=="4":
            designatedLocation(master)
        elif choice=="5":
            closeup(master)
            break
        else:
            print("Invalid choice. Please try again.\n")
except:
    print("error")