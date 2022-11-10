s = str(input())

count1 = 0
count2 = 0
# a = ""
for i in range(len(s)):
    a = s[i]
    if a.isupper():
        count1 +=1
    if a.islower():
        count2 += 1

print('so chu cai in hoa: ', count1)
print('so chu cai in thuong: ',count2)

