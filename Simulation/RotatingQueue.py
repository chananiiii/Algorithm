'''
백준 1021번 - 회전하는 큐
'''

import sys
import queue
deque = []
length, case = map(int, sys.stdin.readline().split())
temp = list(map(int, sys.stdin.readline().split()))
for i in range(1, length + 1) :
    deque.append(i)


total = 0
for i in range(len(temp)) :
    target = temp[i]
    index = 0
    for j in range(len(deque)) :
        if deque[j] == target :
            index = j
            break
    if index < len(deque) - index :
        for k in range(index) :
            temp1 = deque[0]
            del deque[0]
            deque.append(temp1)
        del deque[0]
        total += index
    else :
        for m in range(len(deque) - 1, index, -1) :
            temp1 = deque[len(deque) - 1]
            del deque[(len(deque) - 1)]
            deque.insert(0, temp1)
        del deque[len(deque) - 1]
        total += len(deque) - index + 1

print(total)