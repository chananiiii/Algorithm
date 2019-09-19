'''
백준 1309번 - 동물원
'''


import sys
import queue
sys.setrecursionlimit(100000)
number = int(sys.stdin.readline())

'''
dp = [[0] * 2 for _ in range(100001)]
dp[1][0] = 0
dp[1][1] = 1
for i in range(2, number + 1) :
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1] * 2
    dp[i][1] = dp[i - 1][0] + dp[i - 1][1]
'''

deque1 = queue.deque()
deque2 = queue.deque()
deque1.append(0)
deque2.append(1)
temp1 = 0
temp2 = 0
for i in range(2, number + 1) :
    temp1 = deque1.popleft()
    temp2 = deque2.popleft()
    deque1.append(temp1 + 2 * temp2)
    deque2.append(temp1 + temp2)
temp1 = deque1.popleft()
temp2 = deque2.popleft()
print((2 * temp1 + 3 * temp2) % 9901)
