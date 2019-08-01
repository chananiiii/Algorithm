# 2차원배열을 deepcopy했을때는 시간이 초과 됐다고 나와서
# 1차원으로 deepcopy하는 형식으로 하니 시간 초과가 나오지 않았다.
# 이게 맞는 정답이다.

'''
백준 11403번 - 경로 찾기
문제
가중치 없는 방향 그래프 G가 주어졌을 때,
모든 정점 (i, j)에 대해서, i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N (1 ≤ N ≤ 100)이 주어진다.
둘째 줄부터 N개 줄에는 그래프의 인접 행렬이 주어진다.
i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻이다.
i번째 줄의 i번째 숫자는 항상 0이다.

출력
총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력한다.
정점 i에서 j로 가는 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력해야 한다.

예제 입력 1
3
0 1 0
0 0 1
1 0 0

예제 출력 1
1 1 1
1 1 1
1 1 1
'''
import sys
import copy

sys.setrecursionlimit(1000000)

pointNumber = int(sys.stdin.readline())
graph = [[0] * pointNumber for i in range(0, pointNumber, 1)]
visitGraph = [[0] * pointNumber for i in range(0, pointNumber, 1)]
visit = [0 for i in range(0, pointNumber, 1)]

for i in range(0, pointNumber, 1) :
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(0, pointNumber, 1) :
        graph[i][j] = temp[j]



def dfs(visit, startPoint, endPoint, currentPoint, firstStep) :
    global pointNumber
    global resultGraph
    global graph
    global visitGraph

    if visitGraph[startPoint][endPoint] is 1:
        return

    if endPoint == currentPoint and firstStep == 2 :
        visitGraph[startPoint][currentPoint] = 1
        return

    for i in range(0, pointNumber, 1) :
        if graph[currentPoint][i] is 1 :
            if visit[i] is 1 :
                continue
            else :
                visit[i] = 1
                dfs(visit, startPoint, endPoint, i, 2)

for i in range(0, pointNumber, 1) :
    for j in range(0, pointNumber, 1) :
        dfs(copy.deepcopy(visit), i, j, i, 1)

for i in range(0, pointNumber, 1) :
    for j in range(0, pointNumber, 1) :
        print(visitGraph[i][j], end=' ')
    print()