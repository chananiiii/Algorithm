'''
백준 2206번 - 벽부수고 이동하기

문제

N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고,
1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데,
이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데,
이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면,
벽을 한 개 까지 부수고 이동하여도 된다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다.
다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

예제 입력 1
 6 4
0100
1110
1000
0000
0111
0000

예제 출력 1
15

예제 입력 2
 4 4
0111
1111
1111
1110

예제 출력 2
 -1


'''

import sys
import queue

deque = queue.deque()
sero, garo = map(int, sys.stdin.readline().split())
graph = [[0] * garo for _ in range(sero)]
step = 2
result = 10000
checkGraph = [[0] * garo for _ in range(sero)]


for i in range(sero) :
    temp = sys.stdin.readline()
    for j in range(garo) :
        graph[i][j] = int(temp[j])

''' 모든벽을 하나하나 다 뿌숴서 BFS돌리니까 시간초과가 났음.
def bfs() :
    global sero, garo, graph, deque, step, result
    while len(deque) != 0:
        y, x, count = deque.popleft()
        if y == sero - 1 and x == garo - 1 :
            if result > count :
                result = count
            return

        if y + 1 < sero and graph[y + 1][x] != 1 and graph[y + 1][x] < step:
            deque.append([y + 1, x, count + 1])
            graph[y + 1][x] = step
        if x + 1 < garo and graph[y][x + 1] != 1 and graph[y][x + 1] < step:
            deque.append([y, x + 1, count + 1])
            graph[y][x + 1] = step
        if y - 1 > -1 and graph[y - 1][x] != 1 and graph[y - 1][x] < step:
            deque.append([y - 1, x, count + 1])
            graph[y - 1][x] = step
        if x - 1 > -1 and graph[y][x - 1] != 1 and graph[y][x - 1] < step:
            deque.append([y, x - 1, count + 1])
            graph[y][x - 1] = step

deque.append([0, 0, 1])
bfs()
graph[0][0] = step

for i in range(sero) :
    for j in range(garo) :
        if graph[i][j] == 1 :
            graph[i][j] = 0
            deque.append([0, 0, 1])
            step = step + 1
            graph[0][0] = step
            bfs()
            graph[i][j] = 1

if result == 10000 :
    print(-1)
else :
    print(result)
'''

def bfs() :
    global garo, sero, deque, checkGraph, graph, result
    while len(deque) != 0 :
        '''
        for i in range(sero) :
            for j in range(garo) :
                print(checkGraph[i])
        print()
        '''
        y ,x , count, breaking = deque.popleft()
        if y == sero -1 and x == garo -1 :
            if result > count :
                result = count
                return
        #right
        if breaking == False :
            if x + 1 < garo and graph[y][x + 1] == 0 :
                if checkGraph[y][x + 1] == 0:
                    checkGraph[y][x + 1] = 1
                    deque.append([y, x + 1, count + 1, False])
                if checkGraph[y][x + 1] == 2:
                    checkGraph[y][x + 1] = 3
                    deque.append([y, x + 1, count + 1, False])
            if x + 1 < garo and graph[y][x + 1] == 1 :
                checkGraph[y][x + 1] = 2
                deque.append([y, x + 1, count + 1, True])
        if breaking == True :
            if x + 1 < garo and graph[y][x + 1] == 0 and checkGraph[y][x + 1] == 0:
                checkGraph[y][x + 1] = 2
                deque.append([y, x + 1, count + 1, True])

        #down
        if breaking == False :
            if y + 1 < sero and graph[y + 1][x] == 0 :
                if checkGraph[y + 1][x] == 0:
                    checkGraph[y + 1][x] = 1
                    deque.append([y + 1, x, count + 1, False])
                if checkGraph[y + 1][x] == 2:
                    checkGraph[y + 1][x] = 3
                    deque.append([y + 1, x, count + 1, False])
            if y + 1 < sero and graph[y + 1][x] == 1 :
                checkGraph[y + 1][x] = 2
                deque.append([y + 1, x, count + 1, True])
        if breaking == True :
            if y + 1 < sero and graph[y + 1][x] == 0 and checkGraph[y + 1][x] == 0:
                checkGraph[y + 1][x] = 2
                deque.append([y + 1, x, count + 1, True])

        #left
        if breaking == False :
            if x - 1 > -1 and graph[y][x - 1] == 0 :
                if checkGraph[y][x - 1] == 0:
                    checkGraph[y][x - 1] = 1
                    deque.append([y, x - 1, count + 1, False])
                if checkGraph[y][x - 1] == 2:
                    checkGraph[y][x - 1] = 3
                    deque.append([y, x - 1, count + 1, False])
            if x - 1 > -1 and graph[y][x - 1] == 1 :
                checkGraph[y][x - 1] = 2
                deque.append([y, x - 1, count + 1, True])
        if breaking == True :
            if x - 1 > -1 and graph[y][x - 1] == 0 and checkGraph[y][x - 1] == 0:
                checkGraph[y][x - 1] = 2
                deque.append([y, x - 1, count + 1, True])
        #up
        if breaking == False :
            if y - 1 > -1 and graph[y - 1][x] == 0 :
                if checkGraph[y - 1][x] == 0:
                    checkGraph[y - 1][x] = 1
                    deque.append([y - 1, x, count + 1, False])
                if checkGraph[y - 1][x] == 2:
                    checkGraph[y - 1][x] = 3
                    deque.append([y - 1, x, count + 1, False])
            if y - 1 > -1 and graph[y - 1][x] == 1 :
                checkGraph[y - 1][x] = 2
                deque.append([y - 1, x, count + 1, True])
        if breaking == True :
            if y - 1 > -1 and graph[y - 1][x] == 0 and checkGraph[y - 1][x] == 0:
                checkGraph[y - 1][x] = 2
                deque.append([y - 1, x, count + 1, True])

deque.append([0, 0, 1, False]) # 0,0 에서 시작 False는 아직 한번도 안뚫었다는 의미다.
checkGraph[0][0] = 1 # 먼저 들어가기 전에 체크를 한다.
bfs()

if result == 10000 :
    print(-1)
else :
    print(result)