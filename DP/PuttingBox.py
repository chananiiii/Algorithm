'''
1965번 백준 - 상자넣기
'''
import sys

number = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))
boxArray = [0 for _ in range(number + 1)]
dpArray = [0 for _ in range(number + 1)]
for i in range(number, 0, -1) :
    boxArray[i] = w[i - 1]

for i in range(1, number + 1) :
    temp = 0
    for k in range(0, i) :
        if boxArray[k] < boxArray[i] :
            temp = max(temp, dpArray[k] + 1)
    dpArray[i] = temp
    for j in range(i + 1, number + 1) :
        if boxArray[i] < boxArray[j] :
            dpArray[j] = max(dpArray[j], temp + 1)

print(max(dpArray))
