#coding: utf-8
a, b = map(int, input().split())

intt_array = [0] * 3
intt_array[0] = a + b
intt_array[1] = a - b
intt_array[2] = a * b
# intt_array[3] =

intt_array.sort(reverse=True)
print(intt_array[0])
