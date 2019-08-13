'''
백준 3055번 - 탈출
문제
사악한 암흑의 군주 이민혁은 드디어 마법 구슬을 손에 넣었고,
그 능력을 실험해보기 위해 근처의 티떱숲에 홍수를 일으키려고 한다.
이 숲에는 고슴도치가 한 마리 살고 있다. 고슴도치는 제일 친한 친구인 비버의 굴로 가능한 빨리 도망가 홍수를 피하려고 한다.
티떱숲의 지도는 R행 C열로 이루어져 있다. 비어있는 곳은 '.'로 표시되어 있고, 물이 차있는 지역은 '*',
돌은 'X'로 표시되어 있다. 비버의 굴은 'D'로, 고슴도치의 위치는 'S'로 나타내어져 있다.
매 분마다 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동할 수 있다. (위, 아래, 오른쪽, 왼쪽) 물도 매 분마다 비어있는 칸으로 확장한다.
물이 있는 칸과 인접해있는 비어있는 칸(적어도 한 변을 공유)은 물이 차게 된다. 물과 고슴도치는 돌을 통과할 수 없다.
또, 고슴도치는 물로 차있는 구역으로 이동할 수 없고, 물도 비버의 소굴로 이동할 수 없다.
티떱숲의 지도가 주어졌을 때, 고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간을 구하는 프로그램을 작성하시오.
고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다. 즉, 다음 시간에 물이 찰 예정인 칸으로 고슴도치는 이동할 수 없다.
이동할 수 있으면 고슴도치가 물에 빠지기 때문이다.

입력
첫째 줄에 50보다 작거나 같은 자연수 R과 C가 주어진다.
다음 R개 줄에는 티떱숲의 지도가 주어지며, 문제에서 설명한 문자만 주어진다. 'D'와 'S'는 하나씩만 주어진다.
출력
첫째 줄에 고슴도치가 비버의 굴로 이동할 수 있는 가장 빠른 시간을 출력한다.
만약, 안전하게 비버의 굴로 이동할 수 없다면, "KAKTUS"를 출력한다.

예제 입력 1
3 3
D.*
...
.S.
예제 출력 1
3

예제 입력 2
3 3
D.*
...
..S
예제 출력 2
KAKTUS

예제 입력 3
3 6
D...*.
.X.X..
....S.
예제 출력 3
6

예제 입력 4
5 4
.D.*
....
..X.
S.*.
....
예제 출력 4
4

출처
'''

import sys
import queue

deque = queue.deque()
finish = 100000
sys.setrecursionlimit(1000000)
sero, garo = map(int, sys.stdin.readline().split())
beaverMap = [[0] * garo for _ in range(sero)]
number = 1
starList = []

def backtracking () :
    global garo, sero, beaverMap, finish, number
    number = 1
    while len(deque) != 0 :

        for i in range(sero) :
            for j in range(garo) :
                if beaverMap[i][j] == '*':
                    starList.append([i, j])

        for h in range(0, len(starList), 1) :
            i, j = starList[h]
            if i + 1 < sero  and beaverMap[i + 1][j] != 'D' and beaverMap[i + 1][j] != 'X' :
                beaverMap[i + 1][j] ='*'
            if j + 1 < garo and beaverMap[i][j + 1] != 'D' and beaverMap[i][j + 1] != 'X' :
                beaverMap[i][j + 1] ='*'
            if i - 1 > -1 and beaverMap[i - 1][j] != 'D' and beaverMap[i - 1][j] != 'X' :
                    beaverMap[i - 1][j] ='*'
            if j - 1 > -1 and beaverMap[i][j - 1] != 'D' and beaverMap[i][j - 1] != 'X' :
                beaverMap[i][j - 1] ='*'

        # down
        tempSpace = 0
        for _ in range(number) :
            y, x, count = deque.popleft()
            if (y + 1 < sero and beaverMap[y + 1][x]) == 'D' or (x + 1 < garo and beaverMap[y][x + 1] =='D') \
                    or (y - 1 > -1 and beaverMap[y - 1][x] == 'D') or (x - 1 > -1 and beaverMap[y][x - 1] == 'D') :
                if finish > count:
                    finish = count + 1

            else :
                if y + 1 < sero and str(beaverMap[y + 1][x]).isdigit() :
                    if beaverMap[y + 1][x] < count + 1 :
                        beaverMap[y + 1][x] = count + 1
                        deque.append([y + 1, x, count + 1])
                        tempSpace = tempSpace + 1
                if y + 1 < sero and beaverMap[y + 1][x] == '.' :
                    beaverMap[y + 1][x] = count + 1
                    deque.append([y + 1, x, count + 1])
                    tempSpace = tempSpace + 1

            #right
                if x + 1 < garo and str(beaverMap[y][x + 1]).isdigit() :
                    if beaverMap[y][x + 1] > count + 1 :
                        beaverMap[y][x + 1] = count + 1
                        deque.append([y, x + 1, count + 1])
                        tempSpace = tempSpace + 1
                if x + 1 < garo and beaverMap[y][x + 1] == '.' :
                    beaverMap[y][x + 1] = count + 1
                    deque.append([y, x + 1, count + 1])
                    tempSpace = tempSpace + 1

                #down
                if y - 1 > -1 and str(beaverMap[y - 1][x]).isdigit() :
                    if beaverMap[y - 1][x] > count + 1 :
                        beaverMap[y - 1][x] = count + 1
                        deque.append([y - 1, x, count + 1])
                        tempSpace = tempSpace + 1
                if y - 1 > -1 and beaverMap[y - 1][x] == '.' :
                    beaverMap[y - 1][x] = count + 1
                    deque.append([y - 1, x, count + 1])
                    tempSpace = tempSpace + 1

                #left
                if x - 1 > -1 and str(beaverMap[y][x - 1]).isdigit() :
                    if beaverMap[y][x - 1] > count + 1 :
                        beaverMap[y][x - 1] = count + 1
                        deque.append([y, x - 1, count + 1])
                        tempSpace = tempSpace + 1
                if x - 1 > -1 and beaverMap[y][x - 1] == '.' :
                    beaverMap[y][x - 1] = count + 1
                    deque.append([y, x - 1, count + 1])
                    tempSpace = tempSpace + 1
        number = tempSpace

locationY, locationX = 0, 0
locationY2, locationX2 = 0, 0
for i in range(sero) :
    temp = sys.stdin.readline()
    for j in range(garo) :
        if temp[j] == 'D' :
            locationY = i
            locationX = j
        if temp[j] == 'S' :
            deque.append([i, j, 0])
            beaverMap[i][j] = 0
            locationY2 = i
            locationX2 = j
        else :
            beaverMap[i][j] = temp[j]

if locationY == locationY2 and locationX == locationX2 :
    print("0")
else :
    backtracking()

    if finish == 100000 :
        print("KAKTUS")
    else :
        print(finish)