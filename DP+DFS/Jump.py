'''
백준 1890번 - 점프
'''

import sys

sys.setrecursionlimit(1000000)

length = int(sys.stdin.readline())
graph = [[0] * length for _ in range(length)]
dp = [[-1] * length for _ in range(length)]

for i in range(length) :
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(length) :
        graph[i][j] = temp[j]
        if graph[i][j] == 0 :
            dp[i][j] = 0

dp[length - 1][length - 1] = 1

def dfsDp(y, x) :
    global graph, dp, length
    jump = graph[y][x]
    one = 0
    two = 0

    if dp[y][x] >= 0 :
        return dp[y][x]

    if x + jump < length :
        one = dfsDp(y, x + jump)
    if y + jump < length :
        two = dfsDp(y + jump, x)

    if one == 0 and two == 0 :
        dp[y][x] = 0
    elif one == 0 and two != 0 :
        dp[y][x] = two
    elif one != 0 and two == 0 :
        dp[y][x] = one
    else :
        dp[y][x] = one + two

    return dp[y][x]

dp[0][0] = dfsDp(0, 0)
print(dp[0][0])
