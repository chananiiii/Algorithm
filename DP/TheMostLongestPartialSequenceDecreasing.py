'''
백준 11722번 - 가장 긴 감소하는 부분 수열
'''
import sys

num = int(sys.stdin.readline())
temp = list(map(int, sys.stdin.readline().split()))
array = [[1] * (num + 1) for _ in range(2)]
for i in range(1, num + 1) :
    array[0][i] = temp[i - 1]


'''
시간초과
def dynamic(array, dp, start) :
    global num
    for i in range(start + 1, num + 1) :
        if array[start] > array[i]:
            if i == num:
                return dp[i] + 1
            dp[i] = max(dynamic(array, dp, i), dp[start])

            if dp[i] > 1:
                return dp[i] + 1
    return 1


for i in range(1, num):
    if dp[i] == 1 :
        dp[i] = dynamic(array, dp, i)

print(max(dp))
'''

for i in range(2, num + 1) :
    for j in range(1, i) :
        if array[0][j] > array[0][i] :
            array[1][i] = max(array[1][j] + 1, array[1][i])

print(max(array[1]))