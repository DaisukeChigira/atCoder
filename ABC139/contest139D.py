#coding: utf-8
from decimal import Decimal
n = int(input())
# n = n-1
answer = 0

answer = (n-1)*n//2

# if n % 2 == 0:
# 	answer = (Decimal(n)+Decimal(1))*(Decimal(n)/2)
# else:
# 	answer = Decimal(n)*((Decimal(n)-Decimal(1))/2) + Decimal(n)

print(answer) 
