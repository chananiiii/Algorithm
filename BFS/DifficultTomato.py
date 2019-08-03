'''
백준 7569번 - 토마토
문제
철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다.
토마토는 아래의 그림과 같이 격자모양 상자의 칸에 하나씩 넣은 다음,
상자들을 수직으로 쌓아 올려서 창고에 보관한다.

창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다.
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다.
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때,
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라.
단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다.
M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다.
둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다.
즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어진다. 각 줄에는 상자 가로줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다.
정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다. 이러한 N개의 줄이 H번 반복하여 주어진다.

출력
여러분은 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다.
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고,
토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

예제 입력 1
5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1

예제 출력 1
-1

예제 입력 2
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0

예제 출력 2
4
'''
import sys
import queue
sys.setrecursionlimit(1000000)

garo, sero, height = map(int, sys.stdin.readline().split())
tomatoMap = [[[0] * garo for _ in range(sero)] for _ in range(height)]
dequeZYXDay = queue.deque()
totalDay = 0
check1 = 0
check2 = 0

def bfs(dequeZYXDay) :
    while len(dequeZYXDay) != 0 :
        Z, Y, X, Day = dequeZYXDay.popleft()
        global totalDay
        totalDay = Day
        if Z + 1 < height and tomatoMap[Z + 1][Y][X] == 0 :
            tomatoMap[Z + 1][Y][X] = 1
            dequeZYXDay.append([Z+1,Y,X,Day+1])
        if Z - 1 > -1 and tomatoMap[Z - 1][Y][X] == 0 :
            tomatoMap[Z - 1][Y][X] = 1
            dequeZYXDay.append([Z-1,Y,X,Day+1])

        if Y + 1 < sero and tomatoMap[Z][Y + 1][X] == 0 :
            tomatoMap[Z][Y + 1][X] = 1
            dequeZYXDay.append([Z,Y+1,X,Day+1])
        if Y - 1 > -1 and tomatoMap[Z][Y - 1][X] == 0 :
            tomatoMap[Z][Y - 1][X] = 1
            dequeZYXDay.append([Z,Y-1,X,Day+1])

        if X + 1 < garo and tomatoMap[Z][Y][X + 1] == 0 :
            tomatoMap[Z][Y][X + 1] = 1
            dequeZYXDay.append([Z,Y,X+1,Day+1])
        if X - 1 > -1 and tomatoMap[Z][Y][X - 1] == 0 :
            tomatoMap[Z][Y][X - 1] = 1
            dequeZYXDay.append([Z,Y,X-1,Day+1])

for i in range(sero * height) :
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(garo) :
        tomatoMap[i // sero][i % sero][j] = temp[j]

for i in range(height) :
    for j in range(sero) :
        for k in range(garo) :
            if tomatoMap[i][j][k] == 1 :
                dequeZYXDay.append([i,j,k,0])
            if tomatoMap[i][j][k] == 0 :
                check1 = check1 + 1

bfs(dequeZYXDay)

for i in range(height) :
    for j in range(sero) :
        for k in range(garo) :
            if tomatoMap[i][j][k] == 0 :
                check2 = check2 + 1

if check1 == 0 :
    print(0)
else :
    if check2 > 0 :
        print(-1)
    else :
        print(totalDay)