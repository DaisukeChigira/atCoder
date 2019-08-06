#coding: utf-8
n = int(input())
answer = 'Yes'
t2 = 0
x2 = 0
y2 = 0
for i in range(n):
	t,x,y = map(int, input().split())
	t = t - t2
	x = x - x2
	y = y - y2
	# tがx+yの時、絶対にたどり着けない
	if t < x+y:
		answer = 'No'
		break
	elif t == x+y:
		# 絶対にたどり着ける
		continue
	elif t > x+y:
		# 余った時間が偶数ならたどりつける
		if (t-(x+y)) % 2 != 0:
			answer = 'No'
			break
	x2 = x
	y2 = y
	t2 = t
    
print(answer)
