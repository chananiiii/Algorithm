'''
백준 1966번 - 프린터 큐
'''

import sys

testcase = int(sys.stdin.readline())
deque = [[] for _ in range(testcase)]
for j in range(testcase) :
    count = 0
    numberOfPaper, wonderLocation = list(map(int, sys.stdin.readline().split()))
    temp = list(map(int, sys.stdin.readline().split()))
    for i in range(numberOfPaper) :
        if i == wonderLocation :
            deque[j].append([1, temp[i]])
        else :
            deque[j].append([0, temp[i]])

    while True :
        a = deque[j][0]
        del deque[j][0]
        test = 0
        for i in range(0, len(deque[j])) :
            if a[1] < deque[j][i][1] :
                test += 1
                break
        if test > 0 :
            deque[j].append(a)
            continue
        count += 1
        if a[0] == 1 :
            break
    print(count)