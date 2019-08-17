#coding: utf-8
# inputArray = list(map(int,input().split()))
inputVal = input()
listArray = [x for x in str(inputVal)]
returnVal = 0

for i in listArray:
    if i == '1':
        returnVal = returnVal + 1
    
print(returnVal)
