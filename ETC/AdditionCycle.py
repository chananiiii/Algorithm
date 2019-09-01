'''
백준 1110번 - 더하기 사이클
'''

import sys

num = int(sys.stdin.readline())
changeNum = num
temp = 0
while temp == 0 or changeNum != num :
    first = int(changeNum / 10)
    second = int(changeNum % 10)
    sum = first + second
    changeNum = (second * 10) + int(sum % 10)
    temp = temp + 1

print(temp)