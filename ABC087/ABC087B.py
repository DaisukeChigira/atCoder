#coding: utf-8
# a = int(input())
# b = int(input())
# c = int(input())
# x = int(input())
a,b,c,x = map(int, [input() for i in range(4)])
answer = 0

for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if i * 500 + j * 100 + k * 50 == x:
                answer = answer + 1
    
print(answer)
