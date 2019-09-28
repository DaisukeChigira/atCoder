#coding: utf-8
n, k = map(int, input().split())
pillers = list(map(int,input().split()))
# n = 0
# k = 0
answer = n - k + 1
aaaa = 0
print('answer'+str(answer))

for i in range(len(pillers)-k+1):
	print('stri'+str(i))
	flg = 0
	for j in range(k-1):
		print('i+j'+str(i+j)+' i+j+1='+str(i+j+1))
		if pillers[i+j] > pillers[i+j+1]:
			flg = 1
	print('flg='+str(flg))
	if flg == 0:
		aaaa += 1
		# print(count)

answer = answer - aaaa + 1
print(answer) 
