'''
백준 11727번 - 2xn타일링2
'''

import sys

n = int(sys.stdin.readline())

array = [0 for _ in range(1001)]
array[1] = 1
array[2] = 3
for i in range(3, n + 1):
    if int(i % 2) == 0 :
        array[i] = (array[i-1] + (2 * array[i-2])) % 10007
    else :
        array[i] = (array[i-1] + (2 * array[i-2])) % 10007

print(array[n] % 10007)