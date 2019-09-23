import sys
sys.setrecursionlimit(1000000)
testcase = int(sys.stdin.readline())

def sumsum(start, last, sumArray) :
    return sumArray[last] - sumArray[start - 1]

def recursion(y, x, array, dp, length, sumArray) :
    if y == x :
        return 0
    if y + 1 == x :
        return array[y] + array[x]
    if dp[y][x] != -1 :
        return dp[y][x]
    for k in range(y, x, 1) :
        if dp[y][x] == -1 :
            dp[y][x] = recursion(y, k, array, dp, length, sumArray) + recursion(k + 1, x, array, dp, length, sumArray) + sumsum(y, x, sumArray)
        else :
            dp[y][x] = min(dp[y][x], recursion(y, k, array, dp, length, sumArray) + recursion(k + 1, x, array, dp, length, sumArray) + sumsum(y, x, sumArray))
    return dp[y][x]

for test in range(testcase) :
    length = int(sys.stdin.readline())
    temp = list(map(int, sys.stdin.readline().split()))
    array = [0 for _ in range(length + 1)]
    for i in range(1, length + 1) :
        array[i] = temp[i - 1]
    dp = [[-1] * (length + 1) for _ in range(length + 1)]
    sumArray = [0 for _ in range(length + 1)]
    sumArray[1] = array[1]
    for i in range(2, length + 1) :
        sumArray[i] = sumArray[i - 1] + array[i]

    print(recursion(1, length, array, dp, length, sumArray))