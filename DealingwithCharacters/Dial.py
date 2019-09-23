'''
백준 5622번 - 다이얼
'''
import sys

array = [1 for _ in range(27)]
temp = 1
for i in range(1, 16) :
    array[i] = 2 + temp
    if i % 3 == 0 :
        temp += 1
array[16], array[17], array[18], array[19] =8, 8, 8, 8
array[20], array[21], array[22] = 9, 9, 9
array[23], array[24], array[25], array[26] =10, 10, 10, 10
string = sys.stdin.readline()
number = 0
for i in range(len(string) - 1) :
    number += array[ord(string[i]) - 64]

print(number)