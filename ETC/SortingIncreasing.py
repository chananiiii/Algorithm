'''
10989번 백준 - 수 정렬하기 3
'''
import sys

case = int(sys.stdin.readline())
array = [0 for _ in range(10001)]

for _ in range(case) :
    array[int(sys.stdin.readline())] += 1

for i in range(10001) :
    if array[i] > 0 :
        for _ in range(array[i]) :
            print(i)
