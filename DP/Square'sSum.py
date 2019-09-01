'''
백준 1699번 - 제곱수의 합
'''

import sys
import math

num = int(sys.stdin.readline())
dp = [0 for _ in range(num + 1)]
for i in range(1, num + 1) :
    dp[i] = i
for i in range(1, int(math.sqrt(num)) + 1) :
    dp[i * i] = 1

for i in range(1, num) :
    for j in range(1, int(math.sqrt(num - i)) + 1) :
        if dp[i + j * j] > dp[i] + 1 :
            dp[i + j * j] = dp[i] + 1

print(dp[num])