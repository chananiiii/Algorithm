'''
백준 2156번 - 포도주 시식
'''
import sys

wineNumber = int(sys.stdin.readline())
array = [0 for _ in range(10001)]
check = [[0] * 2 for _ in range(10001)]
for i in range(wineNumber) :
    array[i + 1] = int(sys.stdin.readline())

check[1][0] = array[1]
check[2][0] = array[2]

maximum = 0

for i in range(1, wineNumber + 1) :
    if i + 1 < wineNumber + 1 and check[i][0] + array[i + 1] > check[i + 1][1] :
        check[i + 1][1] = check[i][0] + array[i + 1]
    if i + 2 < wineNumber + 1 and check[i][0] + array[i + 2] > check[i + 2][0] :
        check[i + 2][0] = check[i][0] + array[i + 2]

    if i + 2 < wineNumber + 1 and check[i][1] + array[i + 2] > check[i + 2][0] :
        check[i + 2][0] = check[i][1] + array[i + 2]

    if i + 1 < wineNumber + 1 and check[i + 1][0] < max(check[i][0], check[i][1]):
        check[i + 1][0] = max(check[i][0], check[i][1])

    maximum = max(check[i][0], check[i][1], maximum)

print(maximum)