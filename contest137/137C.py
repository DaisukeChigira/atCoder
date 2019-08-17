<<<<<<< HEAD
#coding: utf-8
amount = int(input())
strings = list(map(str, [input() for i in range(amount)]))
sum = 0
sum2 = 0

for i in range(len(strings)):
	# print(strings[i])
	abc = list(strings[i])
	abc.sort()
	strings[i] = ''.join(abc)
	# print(strings[i])

strings.sort()

for j in range(len(strings)-1):
	# print(j+1)
	# print(strings[j]+strings[j+1])
	if strings[j] == strings[j+1]:
		sum2 = sum2+1
	else:
		sum = sum + sum2 * (sum2+1) / 2
		sum2 = 0

sum = sum + sum2 * (sum2+1) / 2
print(int(sum))
=======
#coding: utf-8
amount = int(input())
strings = list(map(str, [input() for i in range(amount)]))
sum = 0
sum2 = 0

for i in range(len(strings)):
	# print(strings[i])
	abc = list(strings[i])
	abc.sort()
	strings[i] = ''.join(abc)
	# print(strings[i])

strings.sort()

for j in range(len(strings)-1):
	# print(j+1)
	# print(strings[j]+strings[j+1])
	if strings[j] == strings[j+1]:
		sum2 = sum2+1
	else:
		sum = sum + sum2 * (sum2+1) / 2
		sum2 = 0

sum = sum + sum2 * (sum2+1) / 2
print(int(sum))
>>>>>>> d1ea02c9f55043aea2e406cd5688608689b0edfc
