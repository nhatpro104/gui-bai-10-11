
number = int(input())
list = []

for i in range(number):
    value = int(input())
    list.append(value)

def tong_list(list):
    tong = 0
    for i in range(len(list)):
        tong += list[i]

    return tong
print('tong cac so nguyen trong list: ', tong_list(list))