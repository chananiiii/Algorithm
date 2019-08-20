'''
백준 1330번 - 두수 비교하기
'''

import sys

a, b = map(int, sys.stdin.readline().split())

if a > b :
    print('>')
elif a < b :
    print('<')
else :
    print('==')