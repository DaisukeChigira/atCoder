#coding: utf-8
s = str(input())
t = str(input())
ans = 0
ans1 = -1
# s.sort(reversed=True)
# t.sort(reversed=True)
flg = 0

for i in range(len(t)):
	for j in range(ans1+1,len(s)):
		if t[i] == s[j]:
			flg = 1
			# if j > ans1:
			# print('jが大きい'+str(j))
			# ans = ans - ans1 + j + 1
			ans1 = j
			# else:
			# 	print('jが小さい'+str(j))
			# 	ans = ans + len(s)
			# 	ans1 = j
			break
		# elif t[i] < s[j]:
		# 	flg = 0
		# 	break
	if flg == 0:
		for j in range(0,ans1):
			if t[i] == s[j]:
				flg = 1
				# print('jが小さい'+str(j))
				ans = ans + len(s)
				ans1 = j
				break
				
	if flg == 0:
		ans = -1
		break
	else:
		# ans = ans + ans1
		flg = 0
		# ans1 = 0

if ans == -1:
	print(-1)
else:
	print(ans+ans1+1)