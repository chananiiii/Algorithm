'''
백준 1157번 - 단어공부
'''
import sys

string = sys.stdin.readline()
string = string.upper()
array = [0 for _ in range(26)]
for i in range(len(string) - 1) :
    array[ord(string[i]) - 65] += 1

maximum = 0
result = 0
count = 0
for i in range(len(array)) :
    if maximum < array[i] :
        maximum = array[i]
        result = chr(i + 65)
        count = 0
    elif maximum == array[i] :
        count += 1

if count == 0 :
    print(result)
else :
    print("?")