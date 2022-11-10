num = int(input())
list1 = []
for i in range(num):
    value = int(input())
    list1.append(value)

list2 = []
for i in range(len(list1)):
    if list1[i] % 2 ==1:
        list2.append(list1[i])

print('list cac so le: ', list2)