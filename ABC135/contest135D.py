#coding: utf-8
s = str(input())
p = [-1] * len(s)
count = 0

for i in range(len(s)):
	if s[i] == '?':
		p[i] = p[i] + 1
	else:
		p[i] = s[i]
	if int("".jpin(map(str,p))) % 13 == 5:
		count = count+1

print(" ".join(map(str,p)))
