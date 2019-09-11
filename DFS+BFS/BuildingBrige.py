'''
백준 2146 - 다리만들기
'''

import sys
import queue

sys.setrecursionlimit(1000000)

length = int(sys.stdin.readline())
bridge = [[0] * length for _ in range(length)]

def bfsForChangeingToEachTown(a, townNumber, y, x):
    global length
    a[y][x] = townNumber
    if x + 1 < length and a[y][x + 1] == -1:
        bfsForChangeingToEachTown(a, townNumber, y, x + 1)
    if y + 1 < length and a[y + 1][x] == -1 :
        bfsForChangeingToEachTown(a, townNumber, y + 1, x)
    if x - 1 > -1 and a[y][x - 1] == -1 :
        bfsForChangeingToEachTown(a, townNumber, y, x - 1)
    if y - 1 > -1 and a[y - 1][x] == -1 :
        bfsForChangeingToEachTown(a, townNumber, y - 1, x)
result = 1000000

def dfs(deq, array, i) :
    global result, bridge
    while len(deq) != 0 :
        y, x, bridgeNumber, count = deq.popleft()
        if x + 1 < length and array[y][x + 1] == 0 :
            if bridge[y][x + 1] == 0 :
                array[y][x + 1] = count + 1
                deq.append([y, x + 1, bridgeNumber, count + 1])
            else :
                if bridge[y][x + 1] != bridgeNumber :
                    result = min(result, count)
                    break
        if y + 1 < length and array[y + 1][x] == 0 :
            if bridge[y + 1][x] == 0 :
                array[y + 1][x] = count + 1
                deq.append([y + 1, x, bridgeNumber, count + 1])
            else :
                if bridge[y + 1][x] != bridgeNumber :
                    result = min(result, count)
                    break
        if x - 1 > -1 and array[y][x - 1] == 0 :
            if bridge[y][x - 1] == 0 :
                array[y][x - 1] = count + 1
                deq.append([y, x - 1, bridgeNumber, count + 1])
            else :
                if bridge[y][x - 1] != bridgeNumber :
                    result = min(result, count)
                    break
        if y - 1 > -1 and array[y - 1][x] == 0 :
            if bridge[y - 1][x] == 0 :
                array[y - 1][x] = count + 1
                deq.append([y - 1, x, bridgeNumber, count + 1])
            else :
                if bridge[y - 1][x] != bridgeNumber :
                    result = min(result, count)
                    break

for i in range(length) :
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(length) :
        bridge[i][j] = temp[j]
        if bridge[i][j] == 1 :
            bridge[i][j] = -1

temp = 0
for i in range(length) :
    for j in range(length) :
        if bridge[i][j] == -1 :
            temp += 1
            bfsForChangeingToEachTown(bridge, temp, i, j)

check = [[0 for _ in range(length)] for _ in range(length)]
deque = [queue.deque() for _ in range(temp)]
temp = 1
for i in range(length) :
    for j in range(length) :
        if bridge[i][j] != 0 :
            deque[bridge[i][j] - 1].append([i, j, bridge[i][j], 0])

for i in range(len(deque) - 1) :
    dfs(deque[i], check, i)

if result == 1000000 :
    print(0)
else :
    print(result)

