'''
백준 9461번 - 파도반 수열
'''
import sys
testcase = int(sys.stdin.readline())
temp = [0,1,1,1,2]
for _ in range(testcase) :
    length = int(sys.stdin.readline())
    if length < 5 :
        print(temp[length])
    else :
        array = [0 for _ in range(length + 1)]
        array[1] = 1
        array[2] = 1
        array[3] = 1
        array[4] = 2
        for i in range(5, length + 1):
            array[i] = array[i - 1] + array[i - 5]

        print(array[length])