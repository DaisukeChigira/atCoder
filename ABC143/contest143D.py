#coding: utf-8
from bisect import bisect_left

n = int(input())
poll_list = list(map(int,input().split()))
# strings = list(map(str, [input() for i in range(amount)]))

poll_list.sort()
ans = 0

for i in range(n):
    for j in range(i+1,n):
        idx = bisect_left(poll_list, poll_list[i]+poll_list[j])
        ans += max(0,idx-1)

print(ans)
