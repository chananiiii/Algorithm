'''
백준 9251번 - LCS
'''

import sys

temp1 = str(sys.stdin.readline())
temp2 = str(sys.stdin.readline())



str1 = [0 for _ in range(len(temp1) + 1)]
str2 = [0 for _ in range(len(temp2) + 1)]



for i in range(len(temp1)) :
    str1[i + 1] = temp1[i]
for i in range(len(temp2)) :
    str2[i + 1] = temp2[i]

dp = [[0] * (len(temp1)) for _ in range(len(temp2))]

for i in range(1, len(temp2)) :
    for j in range(1, len(temp1)) :
        if str2[i] == str1[j] :
            dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j - 1])
        else :
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(temp2) - 1][len(temp1) - 1])