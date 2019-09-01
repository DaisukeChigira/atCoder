#coding: utf-8
n,k = map(int, input().split())
stra = list(map(int,input().split()))
strb = []
# for i in range(k):
# 	strb = strb + stra
inner = 0
outer = 0
sss = 0
# print(stra)
# print(strb)

for i in range(len(stra)-1):
	for j in range(i+1,len(stra)):
		print('LR=' + str(stra[i]) + ',' + str(stra[j]))
		if stra[i] > stra[j]:
			inner += 1
print('innergroup=' + str(inner))
inner = inner * k
print('inner=' + str(inner))
for i in range(len(stra)):
	for j in range(len(stra)):
		if stra[i] > stra[j]:
			outer += 1
	# print(inner)
print('outergroup=' + str(outer))
outer = outer * k * (k-1) /2
print('outer=' + str(outer))


# for p in range(k):
# 	sss += p+1
# sss = outer * k * (k-1) /2
# print(sss)
print(round((inner + outer) % (1000000000 + 7)))
