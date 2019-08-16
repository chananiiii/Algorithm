'''
백준 10844번 - 쉬운 계단 수
5
116이 나온다

30
365808847
'''

import sys

N = int(sys.stdin.readline())

array = [[0] * 10 for _ in range(101)]
array[0][0] = 0
for i in range(1, 10) :
    array[0][i] = 1

for i in range(1, N) :
    for j in range(0, 10, 1) :
        if j == 0 :
            array[i][j] = array[i-1][j+1] % 1000000000
        elif j == 9 :
            array[i][j] = array[i-1][j-1] % 1000000000
        else :
            array[i][j] = (array[i-1][j-1] + array[i-1][j+1]) % 1000000000

print((sum(array[N-1])) % 1000000000)