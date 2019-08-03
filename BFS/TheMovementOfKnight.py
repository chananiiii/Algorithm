'''
백준 7562번 - 나이트의 이동

문제
체스판 위에 한 나이트가 놓여져 있다.
나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다.
나이트가 이동하려고 하는 칸이 주어진다.
나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이
l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다.
체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다.
둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 몇 번만에 이동할 수 있는지 출력한다.

예제 입력 1
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1

예제 출력 1
5
28
0
'''

import sys
from collections import deque

sys.setrecursionlimit(1000000)
knightY, knightX, targetY, targetX, xy = 0, 0, 0, 0, 0
testcaseNumber = int(sys.stdin.readline())

def bfs () :
    while True :
        currentY, currentX, currentCount = dequeY.popleft(), dequeX.popleft(), dequeCount.popleft()
        if currentY == targetY and currentX == targetX :
            print(currentCount)
            return
        else :
            if currentY + 2 < xy and currentX + 1 < xy and knightMap[currentY + 2][currentX + 1] == 0:
                knightMap[currentY + 2][currentX + 1] = 1
                dequeY.append(currentY + 2)
                dequeX.append(currentX + 1)
                dequeCount.append(currentCount + 1)
            if currentY + 1 < xy and currentX + 2 < xy and knightMap[currentY + 1][currentX + 2] == 0:
                knightMap[currentY + 1][currentX + 2] = 1
                dequeY.append(currentY + 1)
                dequeX.append(currentX + 2)
                dequeCount.append(currentCount + 1)
            if currentY - 1 > -1 and currentX + 2 < xy and knightMap[currentY - 1][currentX + 2] == 0:
                knightMap[currentY - 1][currentX + 2] = 1
                dequeY.append(currentY - 1)
                dequeX.append(currentX + 2)
                dequeCount.append(currentCount + 1)
            if currentY - 2 > -1 and currentX + 1 < xy and knightMap[currentY - 2][currentX + 1] == 0:
                knightMap[currentY - 2][currentX + 1] = 1
                dequeY.append(currentY - 2)
                dequeX.append(currentX + 1)
                dequeCount.append(currentCount + 1)

            if currentY - 2 > -1 and currentX - 1 > -1 and knightMap[currentY - 2][currentX - 1] == 0:
                knightMap[currentY - 2][currentX - 1] = 1
                dequeY.append(currentY - 2)
                dequeX.append(currentX - 1)
                dequeCount.append(currentCount + 1)
            if currentY - 1 > -1 and currentX - 2 > -1 and knightMap[currentY - 1][currentX - 2] == 0:
                knightMap[currentY - 1][currentX - 2] = 1
                dequeY.append(currentY - 1)
                dequeX.append(currentX - 2)
                dequeCount.append(currentCount + 1)
            if currentY + 1 < xy and currentX - 2 > -1 and knightMap[currentY + 1][currentX - 2] == 0:
                knightMap[currentY + 1][currentX - 2] = 1
                dequeY.append(currentY + 1)
                dequeX.append(currentX - 2)
                dequeCount.append(currentCount + 1)
            if currentY + 2 < xy and currentX - 1 > -1 and knightMap[currentY + 2][currentX - 1] == 0:
                knightMap[currentY + 2][currentX - 1] = 1
                dequeY.append(currentY + 2)
                dequeX.append(currentX - 1)
                dequeCount.append(currentCount + 1)

for _ in range(testcaseNumber) :
    xy = int(sys.stdin.readline())
    knightMap = [[0] * xy for _ in range(xy)]
    dequeY = deque()
    dequeX = deque()
    dequeCount = deque()
    knightY, knightX = map(int, sys.stdin.readline().split())
    targetY, targetX = map(int, sys.stdin.readline().split())
    dequeY.append(knightY)
    dequeX.append(knightX)
    dequeCount.append(0)
    knightMap[knightY][knightX] = 1
    bfs()