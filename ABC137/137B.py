<<<<<<< HEAD
#coding: utf-8
k, x = map(int, input().split())

answer = []
for i in (range(x-k+1,x+k)):
    # print(i)
    if x+i >= -10000 and i <= 10000:
        # print(i)
        answer.append(i)

print(" ".join(map(str,answer)))
=======
#coding: utf-8
k, x = map(int, input().split())

answer = []
for i in (range(x-k+1,x+k)):
    # print(i)
    if x+i >= -10000 and i <= 10000:
        # print(i)
        answer.append(i)

print(" ".join(map(str,answer)))
>>>>>>> d1ea02c9f55043aea2e406cd5688608689b0edfc
