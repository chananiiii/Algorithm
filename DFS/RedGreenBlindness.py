#백준 10026번 - 적록색약

'''

문제
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다.
따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.
크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다.
그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다.
또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다.
(색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1)
하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)
그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와
아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄부터 N개 줄에는 그림이 주어진다.

출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

예제 입력 1
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

예제 출력 1
4 3
'''


import sys

sys.setrecursionlimit(1000000)
a = int(sys.stdin.readline())
graphForNomal= [([0] * a) for _ in range(a)]
graphForRedGreen= [([0] * a) for _ in range(a)]
count_Nomal = 0
count_Red_Green = 0

for i in range(a) :
    str = sys.stdin.readline()
    for j in range(a) :
        graphForNomal[i][j] = str[j]
        if str[j] == "R" :
            graphForRedGreen[i][j] = "G"
        else :
            graphForRedGreen[i][j] = str[j]

def nomal_Dfs(graph, color, sero, garo) :
    if garo + 1 < a and (color == graph[sero][garo + 1]):
        graph[sero][garo + 1] = "A"
        nomal_Dfs(graph, color, sero, garo + 1)

    if sero + 1 < a and (color == graph[sero + 1][garo]) :
        graph[sero + 1][garo] = "A"
        nomal_Dfs(graph, color, sero + 1, garo)

    if garo - 1 > -1 and (color == graph[sero][garo - 1]) :
        graph[sero][garo - 1] = "A"
        nomal_Dfs(graph, color, sero, garo - 1)

    if sero - 1 > -1 and (color == graph[sero - 1][garo]) :
        graph[sero - 1][garo] = "A"
        nomal_Dfs(graph, color, sero - 1, garo)

#이거 필요 없을듯..?
'''
def red_Green_Dfs(color, sero, garo) :
    if garo + 1 < a and ()
'''

for i in range(a) :
    for j in range(a) :
        if graphForNomal[i][j] != "A" :
            temp = graphForNomal[i][j]
            graphForNomal[i][j] = "A"
            count_Nomal = count_Nomal + 1
            nomal_Dfs(graphForNomal, temp, i, j)

for i in range(a) :
    for j in range(a) :
        if graphForRedGreen[i][j] != "A" :
            temp = graphForRedGreen[i][j]
            graphForRedGreen[i][j] = "A"
            count_Red_Green = count_Red_Green + 1
            nomal_Dfs(graphForRedGreen, temp, i, j)

print(count_Nomal, end = ' ')
print(count_Red_Green)