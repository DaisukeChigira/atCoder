#coding: utf-8
# from bisect import bisect_left
# from decimal import Decimal
from itertools import combinations

n = int(input())
l = list(map(int,input().split()))
ans = 0

# for i in range(n-1):
#     for j in range(i+1,n):
#         ans += l[i] ^ l[j]

for i, j in combinations(range(n), 2):
    # print(str(i)+str(j))
    ans += l[i] ^ l[j]

print(ans%1000000007)
