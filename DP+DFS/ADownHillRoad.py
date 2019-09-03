'''
백준 1520번 - 내리막길
'''
import sys

sys.setrecursionlimit(1000000)
sero, garo = map(int, sys.stdin.readline().split())

graph = [[10001] * (garo + 2) for _ in range(sero + 2)]
dp = [[-1] * (garo + 2) for _ in range(sero + 2)]
dp[sero][garo] = 1

for i in range(1, sero + 1) :
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(1, garo + 1) :
        graph[i][j] = temp[j - 1]

def dfs(y, x) :
    global sero, garo, graph, dp
    if (dp[y][x] >= 0) :
        return dp[y][x]
    else :
        dp[y][x] = 0
        if graph[y][x] > graph[y][x + 1] :
            dp[y][x] = dp[y][x] + dfs(y, x + 1)
        if graph[y][x] > graph[y + 1][x] :
            dp[y][x] = dp[y][x] + dfs(y + 1, x)
        if graph[y][x] > graph[y][x - 1] :
            dp[y][x] = dp[y][x] + dfs(y, x - 1)
        if graph[y][x] > graph[y - 1][x] :
            dp[y][x] = dp[y][x] + dfs(y - 1, x)

    return dp[y][x]

result = dfs(1, 1)

print(result)