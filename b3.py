
a = 2
b= 1
while a>=b:
    a = int(input('nhap so a: '))
    b = int(input('nhap so b: '))

count1 = 0
count2 = 0
for i in range(a, b+1):
    if i%2==0:
        count1+=1
    if i%2 !=0:
        count2+=1

print('so cac so chan: ', count1)
print('so cac so le: ', count2)