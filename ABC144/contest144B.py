#coding: utf-8
# n,k = int(input())
# list = list(map(int,input().split()))
# strings = list(map(str, [input() for i in range(amount)]))

n = int(input())
ans = 'No'

for i in range(1,10):
    # print(i)
    if n % i == 0 and n // i < 10:
        ans = 'Yes'
        break

print(ans)
