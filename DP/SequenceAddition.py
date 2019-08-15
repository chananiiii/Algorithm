'''
백준 1912번 - 연속합
'''
import sys

number = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

temp = array[0]
maximum = temp

for i in range(0, len(array), 1) :
    if i + 1 < len(array):
        temp = temp + array[i + 1]
        maximum = max(temp, maximum)
    if i + 1 < len(array) and temp < array[i + 1] :
        temp = array[i + 1]
        maximum = max(temp, maximum)

print(maximum)