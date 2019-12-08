#coding: utf-8
# n,k = int(input())
# list = list(map(int,input().split()))
# strings = list(map(str, [input() for i in range(amount)]))
import math

n = int(input())
nn = int(math.sqrt(n) // 1)
ans = 0

for i in reversed(range(1,nn+1)):
    # print(i)
    if n % i == 0:
        ans = (i-1)+(n//i-1)
        break

print(ans)
