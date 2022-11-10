#bt4 anh zalo
num = int(input())
list = []
for i in range(num):
    variable = float(input())
    list.append(variable)


def list_so(list):
    list2 = []
    for i in range(len(list)):
        if bool(list[i]):
            list2.append(list[i])
    return list2


print(" ", list_so(list))




