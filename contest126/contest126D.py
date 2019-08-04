#coding: utf-8
s = str(input())
child = [0] * len(s)
# for j in range(len(s)):
# 	child[j] = 1
r = 0
l = 0
# lIdx = 0
rIdx = 0

for i in range(len(s)):
	# print(str(r)+","+str(l))
	if s[i] == 'R':
		# print(i)
		r = r+1
		if s[i+1] == 'L':
			rIdx = i
	elif s[i] == 'L':
		l = l+1
		if i == len(s)-1 or s[i+1] == 'R':
			#1セットが終了する
			# print('r='+str(r)+" l="+str(l))
			if ((r+l)%2) == 0:
				child[rIdx] = (r+l)//2
				child[rIdx+1] = (r+l)//2
			else:
				if r%2==0:
					child[rIdx+1] = (r+l)//2 + 1
					child[rIdx] = (r+l)//2
				else:
					child[rIdx+1] = (r+l)//2
					child[rIdx] = (r+l)//2 + 1
			r = 0
			l = 0
			# lIdx = i-1
# child[rIdx-1] = l

#roop終わらない解法
# for j in range(10 ** 100):
# 	after = [0] * len(s)
# 	for i in range(len(s)):
# 		# print(i)
# 		if child[i] != 0:
# 			if s[i] == 'R':
# 				after[i+1] = after[i+1] + child[i]
# 				# child[i] = 0
# 			elif s[i] == 'L':
# 				after[i-1] = after[i-1] + child[i]
# 				# child[i] = 0
# 	child = after

print(" ".join(map(str,child)))
