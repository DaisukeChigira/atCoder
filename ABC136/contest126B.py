#coding: utf-8
n = int(input())
ans = 0
for i in range(1,n+1):
    if len(str(i)) % 2 != 0:
        ans = ans + 1
print(ans) 
