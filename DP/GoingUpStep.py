'''
백준 2579번 - 계단 오르기
'''

import sys

a = int(sys.stdin.readline())
step=[0 for _ in range(a + 1)]
checkStep = [[0] * 2 for _ in range(301)]
for i in range(1, a + 1, 1) :
    step[i] = int(sys.stdin.readline())

''' 배열에 한번에 접근하는 식으로 하자

checkStep[1].append([step[1], 1])
for i in range(1, a + 1, 1) :
    for j in checkStep[i] :
        if i + 1 < a + 1 and j[1] + 1 < 3 :
            if [j[0] + step[i + 1], j[1] + 1] not in checkStep[i + 1] :
                checkStep[i + 1].append([j[0] + step[i + 1], j[1] + 1])
        if i + 2 < a + 1 :
            if [j[0] + step[i + 2], 1] not in checkStep[i + 2] :
                checkStep[i + 2].append([j[0] + step[i + 2], 1])

maxResult = 0
for i in checkStep[a] :
    if maxResult < i[0] :
        maxResult = i[0]

print(maxResult)
'''
checkStep[1][0] = step[1]
if a + 1 > 2 :
    checkStep[2][0] = step[2]

for i in range(1, a + 1, 1) :
    if checkStep[i][0] > 0 :
        if i + 1 < a + 1 and checkStep[i][0] + step[i + 1] > checkStep[i + 1][1] :
            checkStep[i + 1][1] = checkStep[i][0] + step[i + 1]
        if i + 2 < a + 1 and checkStep[i][0] + step[i + 2] > checkStep[i + 2][0] :
            checkStep[i + 2][0] = checkStep[i][0] + step[i + 2]

    if checkStep[i][1] > 0 :
        if i + 2 < a + 1 and checkStep[i][1] + step[i + 2] > checkStep[i + 2][0] :
            checkStep[i + 2][0] = checkStep[i][1] + step[i + 2]

print(max(checkStep[a][0], checkStep[a][1]))