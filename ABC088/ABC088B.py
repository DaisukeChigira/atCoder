# codineg: utf-8
n = int(input())
cards = list(map(int,input().split()))
# a,b,c,x = map(int, [input() for i in range(4)])
answer = 0
bob = 0
alice = 0

cards.sort(reverse=True)
for i in range(n):

    # print(i)    
    if i % 2 == 1:
        #bob
        # print("bob cards[i]=" + str(cards[i]))
        bob = bob + cards[i]
    else:
        # print("alice cards[i]=" + str(cards[i]))
        alice = alice + cards[i]
    
print(alice - bob)
