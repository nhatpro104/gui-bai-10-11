print('ax^2+bx+c=0')
print('a = ', end = ' ')
a = int(input())
print('b = ', end = ' ')
b = int(input())
print('c = ', end = ' ')
c = int(input())

# 'math' la mot modun
# modun la mot file chua san cac ham python (=> 1modun == 1 project pycharm ) ( modun giong thu vien trong c++)
# ham duoc khoi tao bang cu phap "def ten_ham" va cac cau lenh owr duoi
# su dung import ta co the dung cac ham da co o nhieu modun khac nhau ( <=> nhieu tep project khac nhau )
# import module1, moduke2, moduleN,...
#       ten_module.<ten_ham>
#   can gi ta truy xuat cai do


import math
x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
print('x1 = ', x1)
print('x2 = ', x2)