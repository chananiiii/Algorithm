'''
백준 2193 - 이친수
dp[i] = dp[i - 1] + dp[i - 2]이다.
왜냐하면, i - 2항의 요소에 각각 뒷부분에 00을 붙이고,
i-1항의 요소에 각각 뒷부분에 1을 붙인 것이
i항을 이루기 때문이다.
'''
import sys

number = int(sys.stdin.readline())

def dp(number) :
    array = [0 for _ in range(91)]
    array[1] = 1
    array[2] = 1
    for i in range(3, number + 1, 1) :
        array[i] = array[i - 2] + array[i - 1]
    return array[number]

print(dp(number))
