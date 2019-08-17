'''
백준 2163번 - 초콜릿 자르기
'''
import sys
sero, garo = map(int, sys.stdin.readline().split())
dp = [[0] * (garo + 2) for _ in range(sero + 2)]

for i in range(1, sero + 1) :
    for j in range(1, garo + 2) :
        if i == 1:
            dp[i][j] = j - 1
        elif j == 1:
            dp[i][j] = i - 1
        else :
            if i % 2 == 0:
                dp[i][j] = dp[int(i / 2)][j] * 2 + 1
            elif j % 2 == 0 :
                dp[i][j] = dp[i][int(j / 2)] * 2 + 1
            else :
                dp[i][j] = dp[int(i/2)][j] + dp[int(i/2 + 1)][j] + 1

print(dp[sero][garo])