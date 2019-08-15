'''
백준 1149번 - RGB거리
'''

import sys

house = int(sys.stdin.readline())

street = list(map(int, sys.stdin.readline().split()))

for i in range(2, house + 1, 1) :
    temp = list(map(int, sys.stdin.readline().split()))
    tempSpace = [1000000 for _ in range(len(temp))]
    for garo in range(0, len(street), 1) :
        for oneMore in range(0, len(tempSpace), 1) :
            if garo != oneMore :
                if tempSpace[oneMore] > (street[garo] + temp[oneMore]) :
                    tempSpace[oneMore] = street[garo] + temp[oneMore]
    for garo in range(0, len(street), 1) :
        street[garo] = tempSpace[garo]
print(min(street))