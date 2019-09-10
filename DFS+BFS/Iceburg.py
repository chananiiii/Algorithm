'''
백준 2574번 - 빙산
'''

import sys
import queue
sys.setrecursionlimit(1000000)
dequeCount = 0
total = 0
sero, garo = map(int, sys.stdin.readline().split())
deque = queue.deque()
tempdeque = queue.deque()
dfsCount = 0
isolated = 0
iceberg = [[0] * garo for _ in range(sero)]
array = [[0] * garo for _ in range(sero)]
oneException = 0

for i in range(sero) :
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(garo) :
        iceberg[i][j] = temp[j]

def bfs() :
    global total, dequeCount, sero, garo, deque, tempdeque, array, dfsCount, isolated
    y, x, original = 0, 0, 0
    while len(deque) != 0 :
        dequeNum = len(deque)
        y, x, original = deque.popleft()
        dfsCount = 0
        dfs(y, x)
        dfsCount += 1
        deque.appendleft([y, x, original])
        if dfsCount != dequeNum :
            isolated = 1
            break
        else :
            total += 1

        while len(deque) != 0 :
            y, x, original = deque.popleft()
            one = 0
            if x + 1 < garo and iceberg[y][x + 1] == 0 :
                one += 1
            if y + 1 < sero and iceberg[y + 1][x] == 0 :
                one += 1
            if x - 1 > -1 and iceberg[y][x - 1] == 0 :
                one += 1
            if y - 1 > -1 and iceberg[y - 1][x] == 0 :
                one += 1

            tempdeque.append([y, x, one])
        while len(tempdeque) != 0:
            y, x, original = tempdeque.popleft()
            if iceberg[y][x] - original <= 0 :
                iceberg[y][x] = 0
            else :
                iceberg[y][x] = iceberg[y][x] - original
                deque.append([y, x, iceberg[y][x]])

def dfs(y, x) :
    global total, dequeCount, sero, garo, deque, tempdeque, array, dfsCount
    array[y][x] = total + 1
    if x + 1 < garo and iceberg[y][x + 1] != 0 and array[y][x + 1] == total :
        array[y][x + 1] = total + 1
        dfs(y, x + 1)
        dfsCount += 1
    if y + 1 < sero and iceberg[y + 1][x] != 0 and array[y + 1][x] == total :
        array[y + 1][x] = total + 1
        dfs(y + 1, x )
        dfsCount += 1
    if x - 1 > -1 and iceberg[y][x - 1] != 0 and array[y][x - 1] == total :
        array[y][x - 1] = total + 1
        dfs(y,  x - 1)
        dfsCount += 1
    if y - 1 > -1 and iceberg[y - 1][x] != 0 and array[y - 1][x] == total :
        array[y - 1][x] = total + 1
        dfs(y - 1, x)
        dfsCount += 1

temp1, temp2 = 0, 0
for i in range(sero) :
    for j in range(garo) :
        if iceberg[i][j] > 0 :
            deque.append([i, j, iceberg[i][j]])

bfs()

if isolated == 1 :
    print(total)
else :
    print(0)