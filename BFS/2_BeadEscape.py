'''
백준 구슬탈출 - 13460번
문제
스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다. 
구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.

보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다. 
가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다. 
빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 
각각 하나씩 들어가 있다. 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다.
 이때, 파란 구슬이 구멍에 들어가면 안 된다.

이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다. 
왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.

각각의 동작에서 공은 동시에 움직인다. 빨간 구슬이 구멍에 빠지면 성공이지만, 
파란 구슬이 구멍에 빠지면 실패이다. 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 
빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다. 
기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.

보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다. 
다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다. 
이 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다. '.'은 빈 칸을 의미하고, 
'#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, 'O'는 구멍의 위치를 의미한다. 'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치이다.

입력되는 모든 보드의 가장자리에는 모두 '#'이 있다. 
구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.

출력
최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다. 
만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.

예제 입력 1 
5 5
#####
#..B#
#.#.#
#RO.#
#####
예제 출력 1 
1
'''
import sys
import queue
sys.setrecursionlimit(1000000)

sero, garo = map(int, sys.stdin.readline().split())
beadMap = [[0] * garo for _ in range(sero)]
checkMap = [[[[0] * garo for _ in range(sero)] for _ in range(garo)] for _ in range(sero)]
redSero, redGaro, blueSero, blueGaro, hallSero, hallGaro = 0, 0, 0, 0, 0, 0
min = 10000
for i in range(sero) :
    temp = sys.stdin.readline()
    for j in range(garo) :
        beadMap[i][j] = temp[j]
        if 'R' == temp[j] :
            redSero = i
            redGaro = j
        if 'B' == temp[j] :
            blueSero = i
            blueGaro = j
        if 'O' == temp[j] :
            hallSero = i
            hallGaro = j

def backTracking(beadMap, count) :
    global redSero, redGaro, blueSero, blueGaro, hallSero, hallGaro, min
    originalRedSero, originalRedGaro, originalBlueSero, originalBlueGaro = redSero, redGaro, blueSero, blueGaro

    #left#
    a = 1
    if beadMap[redSero][redGaro - 1] != '#' or beadMap[blueSero][blueGaro - 1] != '#' :
        if redGaro <= blueGaro:
            while True :
                if beadMap[redSero][redGaro - 1] == 'O':
                    if redSero == blueSero and redGaro < blueGaro :
                        what = 0
                        for h in range(redGaro, blueGaro, 1) :
                            if beadMap[redSero][h] == '#':
                                what = what +1
                        if what == 0 :
                            a = 0
                            break
                        else :
                            if min > count :
                                min = count
                                a = 0
                                break
                    if min > count:
                        min = count
                    a = 0
                    break

                if beadMap[blueSero][blueGaro - 1] == 'O':
                    a = 0
                    break

                if beadMap[redSero][redGaro - 1] == '.':
                    beadMap[redSero][redGaro - 1] = 'R'
                    beadMap[redSero][redGaro] = '.'
                    redGaro = redGaro - 1
                    a = 2

                if beadMap[blueSero][blueGaro - 1] == '.':
                    beadMap[blueSero][blueGaro - 1] = 'B'
                    beadMap[blueSero][blueGaro] = '.'
                    blueGaro = blueGaro - 1
                    a = 2

                if (beadMap[redSero][redGaro - 1] == '#' and beadMap[blueSero][blueGaro - 1] == '#') or (beadMap[redSero][redGaro - 1] == '#' and beadMap[blueSero][blueGaro - 1] == 'R') :
                    break

        if redGaro > blueGaro and a == 1:
            while True:
                if beadMap[redSero][redGaro - 1] == 'O':
                    if min > count:
                        min = count
                    a = 0
                    break

                if beadMap[blueSero][blueGaro - 1] == 'O':
                    a = 0
                    break

                if beadMap[blueSero][blueGaro - 1] == '.' :
                    beadMap[blueSero][blueGaro - 1] = 'B'
                    beadMap[blueSero][blueGaro] = '.'
                    blueGaro = blueGaro - 1
                    a = 2

                if beadMap[redSero][redGaro - 1] == '.' :
                    beadMap[redSero][redGaro - 1] = 'R'
                    beadMap[redSero][redGaro] = '.'
                    redGaro = redGaro - 1
                    a = 2

                if (beadMap[redSero][redGaro - 1] == '#' and beadMap[blueSero][blueGaro - 1] == '#') or (beadMap[redSero][redGaro - 1] == 'B' and beadMap[blueSero][blueGaro - 1] == '#') :
                    break

        if a == 2 and (checkMap[redSero][redGaro][blueSero][blueGaro] > count or checkMap[redSero][redGaro][blueSero][blueGaro] == 0) :
            checkMap[redSero][redGaro][blueSero][blueGaro] = count
            backTracking(beadMap, count + 1)

    beadMap[redSero][redGaro] = '.'
    beadMap[blueSero][blueGaro] = '.'
    beadMap[originalRedSero][originalRedGaro] = 'R'
    beadMap[originalBlueSero][originalBlueGaro] = 'B'
    beadMap[hallSero][hallGaro] = 'O'
    redSero = originalRedSero
    redGaro = originalRedGaro
    blueSero = originalBlueSero
    blueGaro = originalBlueGaro

    #up
    a = 1
    if beadMap[redSero - 1][redGaro] != '#' or beadMap[blueSero - 1][blueGaro] != '#' :
        if redSero <= blueSero:
            while True:
                if beadMap[redSero - 1][redGaro] == 'O':
                    if redGaro == blueGaro and redSero < blueSero :
                        what = 0
                        for h in range(redSero, blueSero, 1) :
                            if beadMap[h][redGaro] == '#':
                                what = what + 1
                        if what == 0 :
                            a = 0
                            break
                        else :
                            if min > count:
                                min = count
                                a = 0
                                break
                    if min > count:
                        min = count
                    a = 0
                    break

                if beadMap[blueSero - 1][blueGaro] == 'O':
                    a = 0
                    break

                if beadMap[redSero - 1][redGaro] == '.' :
                    beadMap[redSero - 1][redGaro] = 'R'
                    beadMap[redSero][redGaro] = '.'
                    redSero = redSero - 1
                    a = 2

                if beadMap[blueSero - 1][blueGaro] == '.' :
                    beadMap[blueSero - 1][blueGaro] = 'B'
                    beadMap[blueSero][blueGaro] = '.'
                    blueSero = blueSero - 1
                    a = 2

                if (beadMap[redSero - 1][redGaro] == '#' and beadMap[blueSero - 1][blueGaro] == '#') or (beadMap[redSero - 1][redGaro] == '#' and beadMap[blueSero - 1][blueGaro] == 'R') :
                        break

        if redSero > blueSero and a == 1:
            while True:
                if beadMap[redSero - 1][redGaro] == 'O':
                    if min > count:
                        min = count
                    a = 0
                    break

                if beadMap[blueSero - 1][blueGaro] == 'O':
                    a = 0
                    break

                if beadMap[blueSero - 1][blueGaro] == '.' :
                    beadMap[blueSero - 1][blueGaro] = 'B'
                    beadMap[blueSero][blueGaro] = '.'
                    blueSero = blueSero - 1
                    a = 2

                if beadMap[redSero - 1][redGaro] == '.' :
                    beadMap[redSero - 1][redGaro ] = 'R'
                    beadMap[redSero][redGaro] = '.'
                    redSero = redSero - 1
                    a = 2

                if (beadMap[redSero - 1][redGaro] == '#' and beadMap[blueSero - 1][blueGaro] == '#') or (beadMap[redSero - 1][redGaro] == 'B' and beadMap[blueSero - 1][blueGaro] == '#'):
                    break

        if a == 2 and (checkMap[redSero][redGaro][blueSero][blueGaro] > count or checkMap[redSero][redGaro][blueSero][blueGaro] == 0) :
            checkMap[redSero][redGaro][blueSero][blueGaro] = count
            backTracking(beadMap, count + 1)


    beadMap[redSero][redGaro] = '.'
    beadMap[blueSero][blueGaro] = '.'
    beadMap[originalRedSero][originalRedGaro] = 'R'
    beadMap[originalBlueSero][originalBlueGaro] = 'B'
    beadMap[hallSero][hallGaro] = 'O'
    redSero = originalRedSero
    redGaro = originalRedGaro
    blueSero = originalBlueSero
    blueGaro = originalBlueGaro

    #right
    a = 1
    if beadMap[redSero][redGaro + 1] != '#' or beadMap[blueSero][blueGaro + 1] != '#':
        if redGaro >= blueGaro:
            while True:
                if beadMap[redSero][redGaro + 1] == 'O':
                    if redSero == blueSero and redGaro > blueGaro :
                        what = 0
                        for h in range(blueGaro, redGaro, 1) :
                            if beadMap[redSero][h] == '#':
                                what = what +1
                        if what == 0 :
                            a = 0
                            break
                        else :
                            if min > count :
                                min = count
                                a = 0
                                break
                    if min > count:
                        min = count
                    a = 0
                    break

                if beadMap[blueSero][blueGaro + 1] == 'O':
                    a = 0
                    break

                if beadMap[redSero][redGaro + 1] == '.' :
                    beadMap[redSero][redGaro + 1] = 'R'
                    beadMap[redSero][redGaro] = '.'
                    redGaro = redGaro + 1
                    a = 2

                if beadMap[blueSero][blueGaro + 1] == '.' :
                    beadMap[blueSero][blueGaro + 1] = 'B'
                    beadMap[blueSero][blueGaro] = '.'
                    blueGaro = blueGaro +1
                    a = 2

                if (beadMap[redSero][redGaro + 1] == '#' and beadMap[blueSero][blueGaro + 1] == '#') or (beadMap[redSero][redGaro + 1] == '#' and beadMap[blueSero][blueGaro + 1] == 'R') :
                    break

        if redGaro < blueGaro and a == 1:
            while True:
                if beadMap[redSero][redGaro + 1] == 'O':
                    if min > count:
                        min = count
                    a = 0
                    break

                if beadMap[blueSero][blueGaro + 1] == 'O':
                    a = 0
                    break

                if beadMap[blueSero][blueGaro + 1] == '.' :
                    beadMap[blueSero][blueGaro + 1] = 'B'
                    beadMap[blueSero][blueGaro] = '.'
                    blueGaro = blueGaro + 1
                    a = 2

                if beadMap[redSero][redGaro + 1] == '.' :
                    beadMap[redSero][redGaro + 1] = 'R'
                    beadMap[redSero][redGaro] = '.'
                    redGaro = redGaro + 1
                    a = 2

                if (beadMap[redSero][redGaro + 1] == '#' and beadMap[blueSero][blueGaro + 1] == '#') or (beadMap[redSero][redGaro + 1] == 'B' and beadMap[blueSero][blueGaro + 1] == '#'):
                    break
        if a == 2 and (checkMap[redSero][redGaro][blueSero][blueGaro] > count or checkMap[redSero][redGaro][blueSero][blueGaro] == 0) :
            checkMap[redSero][redGaro][blueSero][blueGaro] = count
            backTracking(beadMap, count + 1)

    beadMap[redSero][redGaro] = '.'
    beadMap[blueSero][blueGaro] = '.'
    beadMap[originalRedSero][originalRedGaro] = 'R'
    beadMap[originalBlueSero][originalBlueGaro] = 'B'
    beadMap[hallSero][hallGaro] = 'O'
    redSero = originalRedSero
    redGaro = originalRedGaro
    blueSero = originalBlueSero
    blueGaro = originalBlueGaro

    #down
    a = 1
    if beadMap[redSero + 1][redGaro] != '#' or beadMap[blueSero + 1][blueGaro]!= '#':
        if redSero >= blueSero:
            while True:
                if beadMap[redSero + 1][redGaro] == 'O':
                    if redGaro == blueGaro and redSero > blueSero :
                        what = 0
                        for h in range(blueSero, redSero, 1) :
                            if beadMap[h][redGaro] == '#':
                                what = what +1
                        if what == 0 :
                            a = 0
                            break
                        else :
                            if min > count  :
                                min = count
                                a = 0
                                break
                    if min > count:
                        min = count
                    a = 0
                    break

                if beadMap[blueSero + 1][blueGaro] == 'O':
                    a = 0
                    break

                if beadMap[redSero + 1][redGaro] == '.':
                    beadMap[redSero + 1][redGaro] = 'R'
                    beadMap[redSero][redGaro] = '.'
                    redSero = redSero + 1
                    a = 2

                if beadMap[blueSero + 1][blueGaro] == '.' :
                    beadMap[blueSero + 1][blueGaro] = 'B'
                    beadMap[blueSero][blueGaro] = '.'
                    blueSero = blueSero + 1
                    a = 2

                if (beadMap[redSero + 1][redGaro] == '#' and beadMap[blueSero + 1][blueGaro] == '#') or (beadMap[redSero + 1][redGaro] == '#' and beadMap[blueSero + 1][blueGaro] == 'R'):
                    break

        if redSero < blueSero and a == 1:
            while True:
                if beadMap[redSero + 1][redGaro] == 'O':
                    if min > count:
                        min = count
                    a = 0
                    break

                if beadMap[blueSero + 1][blueGaro] == 'O':
                    a = 0
                    break

                if beadMap[blueSero + 1][blueGaro] == '.' :
                    beadMap[blueSero + 1][blueGaro] = 'B'
                    beadMap[blueSero][blueGaro] = '.'
                    blueSero = blueSero + 1
                    a = 2

                if beadMap[redSero +1 ][redGaro] == '.' :
                    beadMap[redSero + 1][redGaro] = 'R'
                    beadMap[redSero][redGaro] = '.'
                    redSero = redSero + 1
                    a = 2

                if (beadMap[redSero + 1][redGaro] == '#' and beadMap[blueSero + 1][blueGaro]) == '#' or (beadMap[redSero + 1][redGaro] == 'B' and beadMap[blueSero + 1][blueGaro] == '#'):
                    break
        if a == 2 and (checkMap[redSero][redGaro][blueSero][blueGaro] > count or checkMap[redSero][redGaro][blueSero][blueGaro] == 0) :
            checkMap[redSero][redGaro][blueSero][blueGaro] = count
            backTracking(beadMap, count + 1)


    beadMap[redSero][redGaro] = '.'
    beadMap[blueSero][blueGaro] = '.'
    beadMap[originalRedSero][originalRedGaro] = 'R'
    beadMap[originalBlueSero][originalBlueGaro] = 'B'
    beadMap[hallSero][hallGaro] = 'O'
    redSero = originalRedSero
    redGaro = originalRedGaro
    blueSero = originalBlueSero
    blueGaro = originalBlueGaro


checkMap[redSero][redGaro][blueSero][blueGaro] = 1
backTracking(beadMap, 1)
if min > 10 :
    print(-1)
else :
    print(min)
    print()