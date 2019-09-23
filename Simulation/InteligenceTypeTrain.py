'''
백준 2455번 - 지능형 기차
'''

import sys

array = [[0] * 2 for _ in range(4)]
totalPeople = 0
for i in range(len(array)) :
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(2) :
        array[i][j] = temp[j]

totalPeople += array[0][1]
maximum = totalPeople
for i in range(1, len(array)) :
    totalPeople -= array[i][0]
    maximum = max(totalPeople, maximum)
    totalPeople += array[i][1]
    maximum = max(totalPeople, maximum)

print(maximum)