testNumber = 0x39
# 0x開頭 or H結尾 = 16進位
# and
#       1       0
# 1   true    flash
# 
# 0   flash   flash

# or
#       1       0
# 1   true    true
# 
# 0   true   flash

# 1 2 3 4 5 6 7 8 9 A B C D E F 
# 1111 1111 1111 1111 = 16位元
# 等於 0039 = 0000 0000 0011 1001  >>4bit = 0000 0000 0000 0011 
# >>移動4bit跟0XF做and        0039 & 000F >> 0011 & 000F >> flash flash flash true 所以只會取3 
                        #    0003 & 000F = 0003   F = 3 
upper = (testNumber>>4) & 0XF
# >>不移動 0011 = 000F  F=9   0039 & 000F >> 0011 & 000F >> flash flash flash true 所以只會取9  只會取true
lower = testNumber & 0XF
# print(16*3+9)
# 1111 = 4bit 
# 1111 1111 1111 1111 =16bit
print(upper)
print(lower)

testNumberUp = 0x1
testNumberDown = 0x13
finalNumber  = (testNumberUp<<4) + testNumberDown

# 0000 0000 0000 0100 

# 0001 0000  

print(finalNumber)
testNumber = 0x10345678
# >>移動16bit  
upper = (testNumber>>16) & 0XFFFF
# >>不移動 0011 1111  =
lower = testNumber& 0XFFFF


print(upper)
print(lower)
testNumberUp = 4148
testNumberDown = 22136

finalNumber  = (testNumberUp<<16) + testNumberDown

print(hex(finalNumber))
