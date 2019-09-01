'''
백준 11055번 - 가장 큰 증가 부분 수열
'''

import sys

length = int(sys.stdin.readline())
dp = [[0] * (length + 1) for _ in range(2)]
temp = list(map(int, sys.stdin.readline().split()))
for i in range(1, length + 1) :
    dp[0][i] = temp[i - 1]
    dp[1][i] = temp[i - 1]

for i in range(1, length + 1) :
    for j in range(i + 1, length + 1) :
        if dp[0][i] < dp[0][j] :
            if dp[1][i] + dp[0][j] > dp[1][j] :
                dp[1][j] = dp[1][i] + dp[0][j]

print(max(dp[1]))