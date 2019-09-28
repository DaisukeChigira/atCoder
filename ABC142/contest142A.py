#coding: utf-8
n = int(input())
ans = 0

if n == 1:
    ans = 1
elif n % 2 == 0:
    ans = 0.5
else:
    ans = ((n-1)/2+1)/n 
print(ans) 
