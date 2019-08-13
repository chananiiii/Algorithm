import sys
import queue
'''
백준 1707 - 이분그래프
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2

2
3 3
1 2
2 3
3 1
2 1
1 2

'''

sys.setrecursionlimit(1000000)
graph = []
checkGraph = []
testcase = int(sys.stdin.readline())
pointNumber, lineNumber = 0, 0
fail = 1

def bfs(deque) :
    global pointNumber, lineNumber, checkGraph, fail, graph
    while len(deque) != 0 :
        y, color = deque.popleft()
        for a in range(0, len(graph[y]), 1) :
            temp = graph[y][a]
            if checkGraph[temp] != 0 and checkGraph[temp] == color :
                fail = 0
                return

            if checkGraph[temp] == 0 and color == 2 :
                checkGraph[temp] = 3
                deque.append([temp, 3])
            if checkGraph[temp] == 0 and color == 3 :
                checkGraph[temp] = 2
                deque.append([temp, 2])

for a in range(testcase) :
    pointNumber, lineNumber = map(int, sys.stdin.readline().split())
    graph = [[] for i in range(pointNumber)]
    checkGraph = [0 for i in range(pointNumber)]
    fail = 1

    for i in range(lineNumber) :
        temp = list(map(int, sys.stdin.readline().split()))
        graph[temp[0] - 1].append(temp[1] - 1)
        graph[temp[1] - 1].append(temp[0] - 1)

    #여기서부터 문제풀이

    y, x = 0, 0
    for i in range(pointNumber) :
        if checkGraph[i] == 0 :
            deque = queue.deque()
            checkGraph[i] = 2
            deque.append([i, 2])
            bfs(deque)



    if fail == 1 :
        print("YES")
    if fail == 0 :
        print("NO")

