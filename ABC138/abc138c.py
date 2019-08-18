#coding: utf-8
n = int(input())
materials = list(map(int,input().split()))
materials.sort()
value = materials[0]

for i in range(1,len(materials)):
	value = (value + materials[i]) /2

print(value)
