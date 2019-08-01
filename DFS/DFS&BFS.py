'''
백준 1260번 - DFS와 BFS
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1
4 5 1
1 2
1 3
1 4
2 4
3 4

예제 출력 1
1 2 4 3
1 2 3 4
'''

import queue

pointNumber, lineNumber, startPointNumber = map(int, input().split())

dfsMap = [[0] * (pointNumber + 2) for j in range(pointNumber + 2)]
bfsMap = [[0] * (pointNumber + 2) for j in range(pointNumber + 2)]

q = queue.Queue()
q.put(startPointNumber)

dfsList = []
bfsList = []

for i in range(1, lineNumber + 1, 1):
    a, b = map(int, input().split())
    dfsMap[a][b] = 1
    dfsMap[b][a] = 1
    bfsMap[a][b] = 1
    bfsMap[b][a] = 1

def dfs(first) :
    if first in dfsList:
        return
    dfsList.append(first)
    print(first, end = ' ')
    for j in range(1, pointNumber + 1, 1):
        if dfsMap[first][j] is not 0 :
            dfsMap[first][j] = 0
            dfsMap[j][first] = 0
            dfs(j)
    return

def bfs() :
    while q.qsize() is not 0:
        first = q.get()
        if first in bfsList:
            continue
        bfsList.append(first)
        print(first, end = " ")
        for j in range(1, pointNumber + 1, 1):
            if bfsMap[first][j] is not 0 :
                q.put(j)

    return

dfs(startPointNumber)
print()
bfs()