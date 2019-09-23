'''
백준 1094번 - 막대기
'''
import sys

initialLength = 64
count = 0
goalLength = int(sys.stdin.readline())
while True :
    if initialLength > goalLength :
        initialLength /= 2
        continue
    elif initialLength < goalLength :
        count += 1
        goalLength -= initialLength
        continue
    else :
        count += 1
        break
print(count)