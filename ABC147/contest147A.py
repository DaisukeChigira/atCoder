#coding: utf-8
# n,k = int(input())
# list = list(map(int,input().split()))
# strings = list(map(str, [input() for i in range(amount)]))

n,k,m = map(int,input().split())
# n,k,m = int(input())
a = n + k + m

if a >= 22:
    l = 'bust'
else:
    l = 'win'

print(l)
