'''
백준 2293번 - 동전1
'''
import sys
coin, worth = list(map(int,sys.stdin.readline().split()))
array = [0 for _ in range(coin + 1)]
for i in range(coin) :
    array[i + 1] = int(sys.stdin.readline())

dp = [0 for _ in range(worth + 1)]
dp[0] = 1
for i in range(1, worth + 1, 1) :
    dp[i] = 0

for i in range(1, coin + 1, 1) :
    temp = [0 for _ in range(worth + 1)]
    for j in range(0, worth + 1, 1) :
        if worth >= array[i] :
            temp[j] = temp[j - array[i]] + dp[j]
        else :
            temp[j] = dp[j]
    dp = temp

print(dp[worth])