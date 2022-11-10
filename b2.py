a = 2
b = 1
while a >= b:
    a = int(input('nhap a: '))
    b = int(input('nhap b: '))

tong = 0
for i in range(a,b,1):
    if (i%2==0):
        tong += i
print('tong cac so can tu a den b: ' + str(tong))








