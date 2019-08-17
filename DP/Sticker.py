'''
백준 9465번 - 스티커
'''

import sys

testcase = int(sys.stdin.readline())
for _ in range(testcase) :
    length = int(sys.stdin.readline())
    dp = [[0] * (length + 2) for _ in range(2)]
    array = [[0] * (length + 2) for _ in range(2)]
    for i in range(2) :
        temp = list(map(int, sys.stdin.readline().split()))
        for j in range(length) :
            array[i][j] = temp[j]
            #dp[i][j] = temp[j]

    #From here, Start the problem. Here I go
    dp[0][0] = array[0][0]
    dp[1][0] = array[1][0]
    for garo in range(0, length) :
        for sero in range(2) :
            if dp[sero][garo] + array[(sero + 1) % 2][garo + 1] > dp[(sero + 1) % 2][garo + 1] :
                dp[(sero + 1) % 2][garo + 1] = dp[sero][garo] + array[(sero + 1) % 2][garo + 1]
            if dp[sero][garo] + array[(sero + 1) % 2][garo + 2] > dp[(sero + 1) % 2][garo + 2] :
                dp[(sero + 1) % 2][garo + 2] = dp[sero][garo] + array[(sero + 1) % 2][garo + 2]


    print(max(dp[0][length], dp[1][length]))
