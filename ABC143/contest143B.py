#coding: utf-8
n = int(input())
takoyaki_list = list(map(int,input().split()))
# strings = list(map(str, [input() for i in range(amount)]))
sum = 0

for i in range(len(takoyaki_list)-1):
    for j in range(i+1,len(takoyaki_list)):
        # print(str(i)+str(',')+str(j))
        sum += takoyaki_list[i]*takoyaki_list[j]
        
print(sum)
