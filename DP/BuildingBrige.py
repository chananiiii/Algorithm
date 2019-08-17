'''
백준 1010번 - 다리놓기
'''
import sys

testcase = int(sys.stdin.readline())

def a(what) :
    sum = 0
    for i in range(1, what + 1):
        sum = i + sum
    return sum

for _ in range(testcase) :
    left, right = map(int, sys.stdin.readline().split())
    array = [[0] * (right + 1) for _ in range(left + 1)]
    for i in range(1, right + 1) :
        array[1][i] = i

    for i in range(2, left + 1) :
        for j in range(i, right + 1) :
            array[i][j] = array[i - 1][j - 1] + array[i][j - 1]

    print(array[left][right])