import sys
import queue

people, connection = map(int, sys.stdin.readline().split())
peopleMap = [[0] * people for _ in range(people)]
deque = queue.deque()
for _ in range(connection) :
    temp = list(map(int, sys.stdin.readline().split()))
    peopleMap[temp[0] - 1][temp[1] - 1] = 1
    peopleMap[temp[1] - 1][temp[0] - 1] = 1

def bfs(i, peopleMap, check) :
    max = 0
    deque.append([i, 0])
    check[i] = 1
    while len(deque) != 0 :
        temp, count = deque.popleft()
        for j in range(people) :
            if check[j] == 0 and peopleMap[temp][j] == 1 :
                deque.append([j, (count + 1)])
                check[j] = 1
                max = count + 1 + max
    return max

temp = 10000
result = 0
for i in range(people) :
    a = bfs(i, peopleMap, [0 for _ in range(people)])
    if temp > a :
        result = i
        temp = a
print(result + 1)

