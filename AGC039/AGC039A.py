#coding: utf-8
strings = str(input())
k = int(input())
s = strings + strings
# print(s)
count = 0

for i in range(len(s)-1):
	# print('strj'+str(j))
	if s[i] == s[i+1]:
		# print(str('s[i]=') + s[i] + str(' s[i+1]=') + s[i+1])
		count += 1
		# s[i] = str(i)
		s = s[:i+1] + str('A') + s[i+2:]
		# print(s)

# print(count)
ans = count*k//2

# if k % 2 == 0:
# 	count = count * k // 2
# else:
# 	print(count*k//2)
# 	print(count//2)
# 	count = count * k // 2 - (count // 2)
if strings[0] == strings[len(strings)-1] and strings[len(strings)-1] != strings[len(strings)-2]:
	# if k >= 2: 
	# 	ans += (k - 1) // 2
	# else:
	# 	ans += 1
	ans += (k - 1) // 2


print(ans) 
