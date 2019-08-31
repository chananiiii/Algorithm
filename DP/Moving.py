'''
백준 이동하기 - 11048
'''

import sys

sero, garo = map(int, sys.stdin.readline().split())
movingMap = [[0] * (garo + 1) for _ in range(sero + 1)]

for i in range(1, sero + 1) :
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(1, garo + 1) :
        movingMap[i][j] = temp[j - 1]

for i in range(1, sero + 1) :
    for j in range(1, garo + 1) :
        movingMap[i][j] = max(movingMap[i - 1][j], movingMap[i][j - 1]) + movingMap[i][j]

print(movingMap[sero][garo])