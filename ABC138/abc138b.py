#coding: utf-8
n = int(input())
numbers = list(map(int,input().split()))
sum = 0
ans = 0

for i in range(len(numbers)):
	sum = sum + 1 / numbers[i]

ans = 1 / sum

print(ans)
