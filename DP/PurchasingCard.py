'''
백준 11052 - 카드구매
'''

import sys

N = int(sys.stdin.readline())
temp = list(map(int, sys.stdin.readline().split()))
array = [0 for _ in range(N + 1)]

for i in  range(1, N + 1) :
    array[i] = temp[i - 1]

for i in range(1, N + 1) :
    for j in range(i + 1, N + 1) :
        if array[j] < array[j-i] + array[i] :
            array[j] = array[j-i] + array[i]


print(array[N])