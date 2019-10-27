#coding: utf-8
# n,k = int(input())
# list = list(map(int,input().split()))
# strings = list(map(str, [input() for i in range(amount)]))

a,b = map(int,input().split())
l = a-b*2

if l < 0:
    l = 0

print(l)
