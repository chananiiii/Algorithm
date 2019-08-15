'''
백준 1003 - 피보나치 함수
'''
import sys

testcase = int(sys.stdin.readline())

zeroCount = 0
oneCount = 0
def dynamic(n) :
    global zeroCount, oneCount
    if n == 0 :
        zeroCount = zeroCount + 1
        return 0
    elif n == 1 :
        oneCount = oneCount + 1
        return 1
    else :
        return dynamic(n - 1) + dynamic(n - 2)

def realFibonacci(array, number) :
    array[0][0] = 1
    array[0][1] = 0
    array[1][0] = 0
    array[1][1] = 1
    for i in range(2, number + 1, 1) :
        array[i][0] = array[i - 1][0] + array[i - 2][0]
        array[i][1] = array[i - 1][1] + array[i - 2][1]


for _ in range(testcase) :
    zeroCount = 0
    oneCount = 0
    number = int(sys.stdin.readline())
    array = [[0] * 2 for _ in range(41)]
    realFibonacci(array, number)
    print(array[number][0], end=" ")
    print(array[number][1])

