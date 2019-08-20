'''
백준 14501번 - 퇴사
'''

import sys

days = int(sys.stdin.readline())
array = [[0] * (days + 1) for _ in range(2)]
dynamicProgramming = [0 for _ in range(days + 1)]
for i in range(1, days + 1):
    temp = list(map(int, sys.stdin.readline().split()))
    array[0][i] = temp[0]
    array[1][i] = temp[1]
    if i + array[0][i] < days + 2 :
        dynamicProgramming[i] = temp[1]

maximum = max(dynamicProgramming)

for i in range(1, days + 1) :
    if i + array[0][i] < days + 1 :
        for j in range(i + array[0][i], days + 1) :
            if j + array[0][j] < days + 2:
                a = dynamicProgramming[i] + array[1][j]
                if a > dynamicProgramming[j] :
                    dynamicProgramming[j] = a
                    maximum = max(a, maximum)



print(maximum)
