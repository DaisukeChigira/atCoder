#coding: utf-8
m,d = map(int, input().split())
ans = 0

for i in range(4,m+1):
	for j in range(22,d+1):
		if int(str(j)[0]) >=2 and int(str(j)[1]) >=2 and i == int(str(j)[0]) * int(str(j)[1]):
			ans += 1

print(ans)
