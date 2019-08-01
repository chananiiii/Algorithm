#모든 배열을 복사해서 찾아서 실패함.
#다른 방법 찾아야함.

import sys
sys.setrecursionlimit(1000000)
findOne = 0

pointNumber = int(input())
graph = [[0] * pointNumber for i in range(0, pointNumber, 1)]
resultGraph = [[0] * pointNumber for i in range(0, pointNumber, 1)]

for i in range(0, pointNumber, 1) :
    temp = list(map(int, input().split()))
    for j in range(0, pointNumber, 1) :
        graph[i][j] = temp[j]

def memoryDelete_list(list) :
    del list[:]
    del list

def dfs(graph, startPoint, endPoint, currentPointX) :
    global pointNumber
    global resultGraph

    if endPoint is currentPointX :
        resultGraph[startPoint][endPoint] = 1
        memoryDelete_list(graph)
        return
    if resultGraph[startPoint][endPoint] is 1 :
        memoryDelete_list(graph)
        return

    for i in range(0, pointNumber, 1) :
        if graph[currentPointX][i]is 1 :
            dfs(graph[:], startPoint, endPoint, i)

for i in range(0, pointNumber, 1) :
    for j in range(0, pointNumber, 1) :
        newGraph = graph[:] # not deep copy
        dfs(newGraph, i, j, i)

for i in range(0, pointNumber, 1) :
    for j in range(0, pointNumber, 1) :
        print(resultGraph[i][j], end=' ')
    print()