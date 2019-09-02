'''
백준 2133번 - 타일 채우기
'''

import sys

num = int(sys.stdin.readline())
if num % 2 == 0 :
    num = int(num / 2)
    dp = [0 for _ in range(31)]
    dp[0] = 1
    dp[1] = 3

    for i in range(2, num + 1, 1) :
        dp[i] = dp[i - 1] * 3 + dp[i]
        for j in range(i - 2 , -1, -1) :
            dp[i] = dp[i] + (dp[j] * 2)

    print(dp[num])
else :
    print(0)