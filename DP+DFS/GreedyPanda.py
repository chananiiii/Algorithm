import sys
sys.setrecursionlimit(1000000)
length = int(sys.stdin.readline())

array = [[0] * length for _ in range(length)]
dp = [[0] * length for _ in range(length)]
for i in range(length) :
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(length) :
        array[i][j] = temp[j]


def dfs(y, x, current) :
    global length, array
    a, b, c, d = 0, 0, 0, 0
    if dp[y][x] != 0 :
        return dp[y][x]

    if x + 1 < length and array[y][x + 1] > current :
        a = dfs(y, x + 1, array[y][x + 1]) + 1
    if y + 1 < length and array[y + 1][x] > current :
        b = dfs(y + 1, x, array[y + 1][x]) + 1
    if x - 1 > -1 and array[y][x - 1] > current :
        c = dfs(y, x - 1, array[y][x - 1]) + 1
    if y - 1 > -1 and array[y - 1][x] > current :
        d = dfs(y - 1, x, array[y - 1][x]) + 1
    if a == 0 and b == 0 and c == 0 and d == 0 :
        dp[y][x] = 1
        return dp[y][x]
    else :
        dp[y][x] = max(a, b, c, d)
        return dp[y][x]
big = 0
for i in range(length) :
    for j in range(length) :
        big = max(big, dfs(i, j, array[i][j]))

print(big)