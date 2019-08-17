<<<<<<< HEAD
#coding: utf-8
n = int(input())
boxes = list(map(int,input().split()))
answer = 'Yes'

for i in reversed(range(1,len(boxes))):
	# print(str(i-1)+str(i))
	if boxes[i-1] - boxes[i] > 1:
		answer = 'No'
		break
	elif boxes[i-1] - boxes[i] == 1:
		boxes[i-1] = boxes[i-1] -1

print(answer) 
=======
#coding: utf-8
n = int(input())
boxes = list(map(int,input().split()))
answer = 'Yes'

for i in reversed(range(1,len(boxes))):
	# print(str(i-1)+str(i))
	if boxes[i-1] - boxes[i] > 1:
		answer = 'No'
		break
	elif boxes[i-1] - boxes[i] == 1:
		boxes[i-1] = boxes[i-1] -1

print(answer) 
>>>>>>> d1ea02c9f55043aea2e406cd5688608689b0edfc
