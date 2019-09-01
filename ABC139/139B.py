#coding: utf-8
a,b = map(int, input().split())

count = 0
plug = 1

while plug < b:
	plug += (a-1)
	count += 1

print(count)
