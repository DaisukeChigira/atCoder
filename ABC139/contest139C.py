#coding: utf-8
n = int(input())
pillers = list(map(int,input().split()))
answer = 0
count = 0

for j in range(len(pillers)-1):
	# print('strj'+str(j))
	if pillers[j] >= pillers[j+1]:
		count += 1
		# print(count)
	else:
		if answer < count:
			answer = count
		count = 0
if answer < count:
	answer = count

print(answer) 
