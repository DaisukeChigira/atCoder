#coding: utf-8
import math
m,n = map(int,input().split())
ans = 1

# GCD(Grate Common Divisier) を求める
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

gcd_cnt = gcd(m,n)
# print(gcd_cnt)

# GCDの約数を素因数分解する
flg = 0
i = 2
aaa = gcd_cnt
while i <= gcd_cnt:
    # print(str(i)+str(',')+str(gcd_cnt))
    if gcd_cnt % i == 0:
        flg = 1
        gcd_cnt = gcd_cnt // i
    else:
        if flg == 1:
            ans +=1
            flg = 0
        i+=1
    if i > aaa/2:
        i = aaa
if flg == 1:
    ans += 1

# if m % 2 == 0 and n % 2 == 0:
#     div.append(2)

# for i in range(1,m+1):
#     # print(i)
#     if m % i == 0 and n % i == 0:
#         ans += 1
#         # m = m / i
#         # n = n / i
#         div.append(i)
#         # for j in range(2,len(div)):
#         #     if i % div[j] == 0:
#         #         flg = 1
#         #         break
#         # if flg == 0:
#         #     div.append(i)
#         # else:
#         #     flg = 0
    
# print(" ".join(map(str,div)))
# div.sorted(reversed=True)

# for j in range(1,div[0]):
#     div[0] % j


# # print(len(div))
print(ans)
