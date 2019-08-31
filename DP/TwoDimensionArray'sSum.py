'''
백준 - 2차원 배열의 합 2167
'''

'''
시간초과
import sys

sero, garo = map(int, sys.stdin.readline().split())
array = [[0] * garo for _ in range(sero)]
for i in range(sero) :
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(garo) :
        array[i][j] = temp[j]

iterator = int(sys.stdin.readline())
for i in range(iterator) :
    temp = list(map(int, sys.stdin.readline().split()))
    sum = 0
    for x in range(temp[0] - 1, temp[2]) :
        for y in range(temp[1] - 1, temp[3]) :
            sum = sum + array[x][y]
    print(sum)
'''

import sys

sero, garo = map(int, sys.stdin.readline().split())
array = [[0] * (garo + 1) for _ in range(sero + 1)]
for i in range(1, sero + 1) :
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(1, garo + 1) :
            array[i][j] = temp[j - 1] + array[i][j - 1]

iterator = int(sys.stdin.readline())
for i in range(iterator) :
    temp = list(map(int, sys.stdin.readline().split()))
    sum = 0
    for x in range(temp[0], temp[2] + 1) :
        sum = sum + array[x][temp[3]] - array[x][temp[1] - 1]
    print(sum)