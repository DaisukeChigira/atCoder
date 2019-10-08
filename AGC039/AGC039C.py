#coding: utf-8
n = int(input())
x = int(input())
count = 0

def calc(n,p,startVal,count):
	if p % 2 == 1:
		p = (p-1)//2
	else:
		p = p//2+2**(n-1)
	count += 1
	# print(p)
	# print(count)
	if p == startVal:
		print(count)
		# return count
	else:
		# print(n)
		# print(startVal)
		calc(n,p,startVal,count)

# for i in range(8):
# 	count = calc(n,i,i,count)
calc(n,x,x,count)
# print(count)
