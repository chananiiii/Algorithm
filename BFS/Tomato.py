'''
백준 토마토 - 7576번

철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다.
토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다.
창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다.
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다.
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때,
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라.
단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다.
단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다.
즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다.
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

출력
여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다.
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고,
토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

예제 입력 1
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

예제 출력 1
8
'''

import sys
from collections import deque
sys.setrecursionlimit(1000000)

m, n = map(int, sys.stdin.readline().split())
#m = garo, n = sero

firstCase = 0
tomatoMap = [[0] * m for _ in range(n)]
dequeSero = deque()
dequeGaro = deque()
day = 0
lastSero = 0
lastGaro = 0

def bfs() :
    global lastSero
    global lastGaro
    global day
    while len(dequeGaro) != 0 :
        firstSero = dequeSero.popleft()
        firstGaro = dequeGaro.popleft()
        tomatoMap[firstSero][firstGaro] = 1

        if firstGaro + 1 < m and tomatoMap[firstSero][firstGaro + 1] == 0:
            tomatoMap[firstSero][firstGaro + 1] = 1
            dequeGaro.append(firstGaro + 1)
            dequeSero.append(firstSero)

        if firstSero + 1 < n and tomatoMap[firstSero + 1][firstGaro] == 0 :
            tomatoMap[firstSero + 1][firstGaro] = 1
            dequeGaro.append(firstGaro)
            dequeSero.append(firstSero + 1)

        if firstGaro - 1 > -1 and tomatoMap[firstSero][firstGaro - 1] == 0 :
            tomatoMap[firstSero][firstGaro - 1] = 1
            dequeGaro.append(firstGaro - 1)
            dequeSero.append(firstSero)

        if firstSero - 1 > -1 and tomatoMap[firstSero - 1][firstGaro] == 0 :
            tomatoMap[firstSero - 1][firstGaro] = 1
            dequeGaro.append(firstGaro)
            dequeSero.append(firstSero - 1)

        if lastGaro == firstGaro and lastSero == firstSero and len(dequeGaro) != 0:
            day = day + 1
            lastSero = dequeSero[len(dequeSero) - 1]
            lastGaro = dequeGaro[len(dequeGaro) - 1]

for sero in range(n) :
    temp = list(map(int, sys.stdin.readline().split()))
    for garo in range(m) :
        tomatoMap[sero][garo] = temp[garo]
        if temp[garo] == 1 :
            firstCase = firstCase + 1
            dequeSero.append(sero)
            dequeGaro.append(garo)

if firstCase == m * n :
    print(0)
else :
    test = 0
    lastSero = dequeSero[len(dequeSero) - 1]
    lastGaro = dequeGaro[len(dequeGaro) - 1]
    bfs()
    for i in range(n) :
        for j in range(m) :
            if tomatoMap[i][j] == 0 :
                test = test + 1
    if test > 0 :
        print(-1)
    else :
        print(day)