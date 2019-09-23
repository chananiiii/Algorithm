'''
백준 1018번 - 체스판 다시 칠하기
'''

import sys
sero, garo = map(int, sys.stdin.readline().split())
checkBoard = [[0] * garo for _ in range(sero)]
for i in range(sero) :
    temp = sys.stdin.readline()
    for j in range(garo) :
        checkBoard[i][j] = temp[j]
final = 1000
for i in range(sero - 7) :
    for j in range(garo - 7):
        firstColor = 'W'
        count = 0
        for x in range(8):
            if (x + i) % 2 == 0:
                for y in range(8):
                    if (y + i) % 2 == 0 and checkBoard[i + x][j + y] != firstColor:
                        count += 1
                    if (y + i) % 2 == 1 and checkBoard[i + x][j + y] == firstColor:
                        count += 1
            else:
                for y in range(8):
                    if (y + i) % 2 == 0 and checkBoard[i + x][j + y] == firstColor:
                        count += 1
                    if (y + i) % 2 == 1 and checkBoard[i + x][j + y] != firstColor:
                        count += 1
        final = min(final, count)
        firstColor = 'B'
        count = 0
        for x in range(8):
            if (x + i) % 2 == 0:
                for y in range(8):
                    if (y + i) % 2 == 0 and checkBoard[i + x][j + y] != firstColor:
                        count += 1
                    if (y + i) % 2 == 1 and checkBoard[i + x][j + y] == firstColor:
                        count += 1
            else:
                for y in range(8):
                    if (y + i) % 2 == 0 and checkBoard[i + x][j + y] == firstColor:
                        count += 1
                    if (y + i) % 2 == 1 and checkBoard[i + x][j + y] != firstColor:
                        count += 1
        final = min(final, count)

print(final)