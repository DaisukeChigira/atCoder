#coding: utf-8
# n,k = int(input())
# list = list(map(int,input().split()))
# strings = list(map(str, [input() for i in range(amount)]))

s = input()
hug = 0

for i in range(len(s)//2):
    # print(i)
    if s[i] != s[len(s)-i-1]:
        hug += 1

print(hug)
