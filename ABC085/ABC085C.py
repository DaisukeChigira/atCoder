#coding: utf-8
n,m = map(int, input().split())
x = -1
y = -1
z = -1

for p in reversed(range(0,n+1)):
	for q in reversed(range(0,n+1-p)):
		if p * 10000 + q * 5000 + (n-p-q) * 1000 == m:
			# print("P,Q,S="+str(p)+","+str(q))
			x = p
			y = q
			z = n-p-q
			break

	if x != -1:
		break

print(str(x) + " " + str(y) + " " + str(z))
