#coding: utf-8
# from decimal import Decimal
n = int(input())
games = list(map(int, [input() for i in range(n)]))

for i in range(games-1):
	for j in range(1,games):
		if games[i][0] == games[j][0]:
			# remove[]

# print(int(round(answer,0))) 
