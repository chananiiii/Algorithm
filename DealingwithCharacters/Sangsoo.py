'''
백준 2908 - 상수
'''
import sys
number = list(map(str, sys.stdin.readline().split()))
temp = 0
for i in range(len(number)) :
    what = 0
    for j in range(len(number[i])) :
        what += int(number[i][j]) * pow(10, j)
    temp = max(temp, what)

print(temp)