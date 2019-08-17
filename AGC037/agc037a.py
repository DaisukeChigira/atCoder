#coding: utf-8
s = str(input())
ans = 1
flg = 0

for i in range(1,len(s)):
	# print(str(s[i-1])+","+str(s[i]))
	if flg == 2:
		ans = ans + 1
		flg = 0
	elif flg == 1:
		# print("aa")
		# ans = ans+1
		flg = 2
	elif s[i] != s[i-1]:
		# print(i)
		ans = ans+1
	else:
		if i != len(s)-1:
			ans = ans+1
			# print("z")
		flg = 1
	# print(str(i)+" "+str(ans))
# if flg > 0:
# 	ans = ans+1

print(ans)
