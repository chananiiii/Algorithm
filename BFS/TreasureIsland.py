'''
백준 2589번 - 보물섬
문제
보물섬 지도를 발견한 후크 선장은 보물을 찾아나섰다. 보물섬 지도는 아래 그림과 같이 직사각형 모양이며
여러 칸으로 나뉘어져 있다. 각 칸은 육지(L)나 바다(W)로 표시되어 있다.
이 지도에서 이동은 상하좌우로 이웃한 육지로만 가능하며, 한 칸 이동하는데 한 시간이 걸린다.
 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다.
 육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안 된다.

예를 들어 위와 같이 지도가 주어졌다면 보물은 아래 표시된 두 곳에 묻혀 있게 되고,
이 둘 사이의 최단 거리로 이동하는 시간은 8시간이 된다.

보물 지도가 주어질 때, 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간을 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 보물 지도의 세로의 크기와 가로의 크기가 빈칸을 사이에 두고 주어진다.
이어 L과 W로 표시된 보물 지도가 아래의 예와 같이 주어지며, 각 문자 사이에는 빈 칸이 없다.
보물 지도의 가로, 세로의 크기는 각각 50이하이다.

출력
첫째 줄에 보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간을 출력한다.

예제 입력 1
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW

예제 출력 1
8
'''

import sys
import queue

sys.setrecursionlimit(1000000)
sero, garo = map(int, sys.stdin.readline().split())
treasureMap = [[0] * garo for _ in range(sero)]
deque = queue.deque()
max = -1
for i in range(sero) :
    temp = sys.stdin.readline()
    for j in range(garo) :
        if temp[j] == 'L' :
            treasureMap[i][j] = 0
        else :
            treasureMap[i][j] = temp[j]

def bfs(treasureMap, deque, step) :
    global sero, garo, max
    while len(deque) != 0 :
        y, x, count = deque.popleft()
        if (x + 1 < garo) and treasureMap[y][x + 1] != 'W' and (treasureMap[y][x + 1] > step) :
            treasureMap[y][x + 1] = step
            deque.append([y, x + 1, count + 1])
        if (y + 1 < sero) and treasureMap[y + 1][x] != 'W' and (treasureMap[y + 1][x] > step) :
            treasureMap[y + 1][x] = step
            deque.append([y + 1, x, count + 1])
        if (x - 1 > -1) and treasureMap[y][x - 1] != 'W' and (treasureMap[y][x - 1] > step) :
            treasureMap[y][x - 1] = step
            deque.append([y, x - 1, count + 1])
        if (y - 1 > -1) and treasureMap[y - 1][x] != 'W' and (treasureMap[y - 1][x] > step) :
            treasureMap[y - 1][x] = step
            deque.append([y - 1, x, count + 1])
        if max < count :
            max = count

step = -1
for i in range(sero) :
    for j in range(garo) :
        if treasureMap[i][j] != 'W'and treasureMap[i][j] > step :
            treasureMap[i][j] = step
            deque.append([i, j, 0])
            bfs(treasureMap, deque, step)
            step = step - 1



print(max)