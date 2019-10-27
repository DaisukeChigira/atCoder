#coding: utf-8
# n,k = int(input())
# list = list(map(int,input().split()))
# strings = list(map(str, [input() for i in range(amount)]))

a,b = map(int,input().split())
l=0

if a >= 10 or b >= 10:
    l = -1
else:
    l = a*b

print(l)
