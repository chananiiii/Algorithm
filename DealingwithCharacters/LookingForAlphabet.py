'''
백준 10809번 - 알파벳 찾기
'''

import sys

string = sys.stdin.readline()
alphabet = [-1 for _ in range(26)]
for i in range(len(string) - 1) :
    if alphabet[ord(string[i]) - 97] == -1 :
        alphabet[ord(string[i]) - 97] = i

for i in range(len(alphabet)) :
    print(alphabet[i], end = " ")