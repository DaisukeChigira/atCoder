#coding: utf-8
n,q = map(int,input().split())
node_list = list(map(str, [input() for i in range(n-1)]))
q_list = list(map(str, [input() for i in range(q)]))
# materials = list(map(int,input().split()))
node_list.sort()
q_list.sort()
values = [0] * n

for j in range(len(q_list)):
	a,b = map(int, q_list[j].split())
	values[a-1] = values[a-1] + b

for i in range(len(node_list)):
	c,d = map(int, node_list[i].split())
	values[i+1] = values[i+1] + values[c-1]
			
print(" ".join(map(str,values)))
