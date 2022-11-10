num = int(input())
list = []

for i in range(num):
    value = int(input())
    list.append(value)
print(list)

# min = list[0]
# for i in range(len(list)):
#     if list[i] < min:
#         min = list[i]
#
# print('so be nhat: ', min)


print('so be nhat: ', min(list))


