'''
백준 동전2 - 2294번
'''
import sys

n, k = map(int, sys.stdin.readline().split())
coin = [0 for _ in range(n)]
dp = [[0] * 100001 for _ in range(n)]
coin.sort()
for i in range(n) :
    coin[i] = int(sys.stdin.readline())

for i in range(k + 1) :
    if i % coin[0] == 0 :
        dp[0][i] = int(i / coin[0])
for i in range(1, n) :
    for j in range(1, k + 1) :
        if coin[i] > j :
            dp[i][j] = dp[i - 1][j]
        elif coin[i] == j :
            dp[i][j] = 1

        else :
            if dp[i - 1][j] == 0 :
                if dp[i][j - coin[i]] != 0 and dp[i][coin[i]] != 0 :
                    dp[i][j] = dp[i][j - coin[i]] + dp[i][coin[i]]
            else :
                if dp[i][j - coin[i]] != 0 and dp[i][coin[i]] != 0 :
                    dp[i][j] = min(dp[i][j - coin[i]] + dp[i][coin[i]], dp[i - 1][j])
                else :
                    dp[i][j] = dp[i - 1][j]

if dp[n - 1][k] == 0 :
    print(-1)
else :
    print(dp[n - 1][k])


''' 시간초과 코드
for i in range(1, k + 1) :
    for j in range(1, int(i / 2) + 1) :
        if i % 2 == 0 and dp[j] != 0 and dp[i - j] != 0 :
            if dp[i] == 0 :
                dp[i] = dp[j] + dp[i - j]
            else :
                dp[i] = min(dp[i], dp[j] + dp[i - j])
            if j == int(i / 2) :
                if dp[i] == 0 :
                    dp[i] = dp[j] * 2
                else :
                    dp[i] = min(dp[i], dp[j] * 2)

        if i % 2 != 0 and dp[j] != 0 and dp[i - j] != 0 :
            if dp[i] == 0 :
                dp[i] = dp[j] + dp[i - j]
            else :
                dp[i] = min(dp[i], dp[j] + dp[i - j])

if dp[k] != 0 :
    print(dp[k])
else :
    print(-1)
'''