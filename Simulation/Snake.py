'''
백준 3190번 - 뱀
'''
import sys
import queue
direction = 0
second = 0
length = int(sys.stdin.readline())
array = [[0] * (length + 2) for _ in range(length + 2)]
queue = []
<<<<<<< HEAD
#수정되었습니다333333
=======
#수정되었습니다.
>>>>>>> tmp

def add(direction, y, x) :
    if direction % 4 == 0 :
        return [y, x + 1]
    elif directioRotatingArray4.pyn % 4 == 1 :
        return [y + 1, x]
    elif direction % 4 == 2 :
        return [y, x - 1]
    elif direction % 4 == 3 :
        return [y - 1, x]

for i in range(length + 2) :
    for j in range(length + 2) :
        if i == 0 or j == 0 or i == length + 1 or j == length + 1:
            array[i][j] = -1

queue.append([1, 1])
testcase = int(sys.stdin.readline())
array[1][1] = 1

for _ in range(testcase) :
    x, y = map(int, sys.stdin.readline().split())
    array[x][y] = 2

snake = int(sys.stdin.readline())
snakeInformation = []
snakeLength = 1
for i in range(snake) :
    a, b = map(str, sys.stdin.readline().split())
    snakeInformation.append([int(a), b])
q = 0
while True :
    second += 1
    if snakeLength == 1 :
        tailY, tailX = queue[0]
        headY, headX = queue[0]
    else :
        tailY, tailX = queue[0]
        headY, headX = queue[len(queue) - 1]
    a, b = add(direction, headY, headX)

    if array[a][b] != -1 and array[a][b] != 1 :
        if array[a][b] == 2 :
            array[a][b] = 1
            snakeLength += 1
            queue.append([a, b])
        elif array[a][b] == 0 :
            del queue[0]
            array[tailY][tailX] = 0
            array[a][b] = 1
            queue.append([a, b])
    else :
        break

    if q < snake and snakeInformation[q][0] == second :
        if snakeInformation[q][1] == 'L' :
            direction += 3
        elif snakeInformation[q][1] == 'D' :
            direction += 1
        q += 1
print(second)