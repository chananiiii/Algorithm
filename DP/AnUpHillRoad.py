'''
백준 11057번 - 오르막길
'''
# 아래에 있는것 1번 풀이
'''
import sys
sys.setrecursionlimit(1000000)

num = int(sys.stdin.readline())
dp = [[0] * 11 for _ in range(num)]

for i in range(11) :
    dp[0][i] = 1
dp[0][10] = 10

if num == 1 :
    print(dp[0][10])
else :
    for i in range(1, num) :
        temp = 0
        for j in range(11) :
            if j == 0 :
                dp[i][j] = (dp[i - 1][10]) % 10007
            elif j == 10 :
                dp[i][j] = temp
            else :
                dp[i][j] = (dp[i][j - 1] - dp[i - 1][j - 1]) % 10007
            temp = dp[i][j] + temp
    print((dp[num - 1][10]) % 10007)
'''

# 이 아래는 2번풀이
import sys
sys.setrecursionlimit(1000000)

num = int(sys.stdin.readline())
dp = [[0] * 10 for _ in range(num)]

for i in range(10) :
    dp[0][i] = 1

if num == 1 :
    print(sum(dp[num - 1]))
else :
    for k in range(1, num) :
        for i in range(10) :
            for j in range(i, 10) :
                dp[k][i] = (dp[k][i] + dp[k - 1][j]) % 10007
    sys.stdout.write(str(sum(dp[num - 1]) % 10007))

