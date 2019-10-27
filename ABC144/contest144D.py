#coding: utf-8
from bisect import bisect_left
from decimal import Decimal

# n = int(input())
a,b,x = map(int,input().split())
vol = Decimal(a*a*b)
h = Decimal(x / (a**2))
p = Decimal(b/a)
ans = Decimal((vol-x)/vol*90*p)

print(ans)
