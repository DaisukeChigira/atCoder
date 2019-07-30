#coding: utf-8
array_length = int(input())
print(array_length)
list_a = list(map(int,input().split()))
print(list_a)

list_b = []
count = 0

for i in list_a:
    print('a')
    if i % 2 == 0:
        print(i / 2)
        list_b.append(i /2)
        count = count + 1
    else:
        break

print(count)
