import sys

n, m, k = map(int, sys.stdin.readline().split())

array = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

def lotation(firstY, firstX, lastY, lastX) :
    global array
    temp1 = array[firstY + 1][firstX]
    temp2 = 0
    for i in range(firstX, lastX + 1) :
        temp2 = array[firstY][i]
        array[firstY][i] = temp1
        temp1 = temp2
    for i in range(firstY + 1, lastY + 1) :
        temp2 = array[i][lastX]
        array[i][lastX] = temp1
        temp1 = temp2
    for i in range(lastX - 1, firstX - 1, -1) :
        temp2 = array[lastY][i]
        array[lastY][i] = temp1
        temp1 = temp2
    for i in range(lastY - 1, firstY, -1) :
        temp2 = array[i][firstX]
        array[i][firstX] = temp1
        temp1 = temp2

for i in range(1, n + 1) :
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(1, m + 1) :
        array[i][j] = temp[j - 1]

final = 0
for _ in range(k) :
    r, c, s = map(int, sys.stdin.readline().split())
    firstY = r - s
    firstX = c - s
    lastY = r + s
    lastX = c + s
    length = lastX - firstX + 1

    for i in range(1, int((length / 2) + 1)) :
        lotation(firstY, firstX, lastY, lastX)
        firstY += 1
        firstX += 1
        lastY -= 1
        lastX -= 1

    for i in range(1, n + 1) :
        if final == 0 :
            final = sum(array[i])
        else :
            final = min(final, sum(array[i]))

print(final)