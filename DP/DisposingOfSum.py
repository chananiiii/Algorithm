'''
백준 2225번 - 합분해
'''

import sys

N, K = list(map(int, sys.stdin.readline().split()))

dp = [[0] * (200 + 1) for _ in range(201)]
for i in range(1, 201) :
    dp[1][i] = i
    dp[i][1] = 1

for i in range(2, 201) :
    for j in range(2, 201) :
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000

print((dp[N][K]) % 1000000000)