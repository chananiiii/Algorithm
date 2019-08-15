'''
백준 11726 - 2xn 타일링
'''
import sys

number = int(sys.stdin.readline())
array = [0 for _ in range(1001)]
array[0] = 0
array[1] = 1
array[2] = 2
for i in range (3, number + 1, 1) :
    array[i] = array[i - 1] + array[i - 2]

print(array[number] % 10007)