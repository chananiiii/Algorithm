import sys

sero, garo = map(int, sys.stdin.readline().split())
dp = [[0] * garo for _ in range(sero)]

big = 0

for i in range(sero) :
    temp = sys.stdin.readline()
    for j in range(garo) :
        dp[i][j] = int(temp[j])
        if dp[i][j] == 1 :
            big = 1

for i in range(sero) :
    for j in range(garo) :
        if j - 1 > -1 and i -1 > -1 and dp[i][j] != 0 and dp[i - 1][j] != 0 and dp[i][j - 1] != 0 and dp[i - 1][j - 1] != 0 :
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            big = max(big, dp[i][j])


print(big * big)