#coding: utf-8
n = int(input())
s = str(input())
# list = list(map(int,input().split()))
# strings = list(map(str, [input() for i in range(amount)]))
count = 1

for i in range(1,n):
    if s[i-1] != s[i]:
        count += 1

print(count)

