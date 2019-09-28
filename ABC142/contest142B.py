#coding: utf-8
n,k = map(int,input().split())
friends = list(map(int,input().split()))

friends.sort(reverse=True)
ans = 0

for i in range(n):
    # print(student[i]-1)
    if friends[i]>=k:
        ans += 1

print(ans) 
