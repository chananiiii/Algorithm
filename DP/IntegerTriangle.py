import sys

layer = int(sys.stdin.readline())
triangle = [[0] * 501 for _ in range(501)]
dp = [[0] * 501 for _ in range(501)]

for i in range(1, layer + 1) :
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(len(temp)) :
        triangle[i][j + 1] = temp[j]

dp[1][1] = triangle[1][1]

for i in range(2, layer + 1) :
    for j in range(1, i + 1) :
        dp[i][j] = max(dp[i - 1][j - 1] + triangle[i][j], dp[i - 1][j] + triangle[i][j])

print(max(dp[layer]))

'''
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
'''