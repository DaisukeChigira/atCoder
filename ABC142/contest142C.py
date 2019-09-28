#coding: utf-8
n = int(input())
student = list(map(int,input().split()))
toukou = [0] * n

for i in range(n):
    # print(student[i]-1)
    toukou[student[i]-1] = i+1
print(" ".join(map(str,toukou))) 
