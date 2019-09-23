import sys

sero, garo, diceY, diceX, order = map(int, sys.stdin.readline().split())
mapmap = [[0] * garo for _ in range(sero)]
diceArray = [0 for _ in range(6)]

def diceChange(direction) :
    global diceArray
    global sero, garo, diceY, diceX
    a0, a1, a2, a3, a4, a5 = diceArray[0], diceArray[1], diceArray[2], diceArray[3], diceArray[4], diceArray[5]
    count = 0
    if direction == 1 and diceX + 1 < garo:
        count += 1
        diceArray[0] = a3
        diceArray[1] = a5
        diceArray[3] = a1
        diceArray[5] = a0
        diceX += 1
    elif direction == 2 and diceX - 1 > -1:
        count += 1
        diceArray[0] = a5
        diceArray[1] = a3
        diceArray[3] = a0
        diceArray[5] = a1
        diceX -= 1
    elif direction == 3 and diceY - 1 > -1:
        count += 1
        diceArray[2] = a5
        diceArray[3] = a2
        diceArray[4] = a3
        diceArray[5] = a4
        diceY -= 1
    elif direction == 4 and diceY + 1 < sero :
        count += 1
        diceArray[2] = a3
        diceArray[3] = a4
        diceArray[4] = a5
        diceArray[5] = a2
        diceY += 1

    if count > 0 :
        return True
    else :
        return False

def change(direction) :
    global sero, garo, diceY, diceX, diceArray, mapmap
    count = 0
    if diceChange(direction) :
        count += 1
        if mapmap[diceY][diceX] == 0 :
            mapmap[diceY][diceX] = diceArray[3]
        else :
            diceArray[3] = mapmap[diceY][diceX]
            mapmap[diceY][diceX] = 0
    if count > 0 :
        return True
    else :
        return False

for i in range(sero) :
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(garo) :
        mapmap[i][j] = temp[j]

orderArray = list(map(int, sys.stdin.readline().split()))

for i in range(order) :

    if change(orderArray[i]) :
        print(diceArray[5])