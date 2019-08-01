'''
백준 - 11403번 경로찾기
눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다.
이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때,
이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.
예를 들어 M=5, N=7 인 모눈종이 위에 <그림 1>과 같이 직사각형 3개를 그렸다면,
그 나머지 영역은 <그림 2>와 같이 3개의 분리된 영역으로 나누어지게 된다.
M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때, K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지,
그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.
'''

import sys
sys.setrecursionlimit(1000000)
input = list(map(int, sys.stdin.readline().split()))
paper = [([0] * (input[0] + 2)) for i in range(input[1] + 2)]
count = 0
territory = []
temp = 0
#바깥쪽 1로 채우는 과정
for i in range(0, 2, 1) :
    for j in range(0, input[0] + 2, 1) :
        paper[0][j] = 1
        paper[input[1] + 1][j] = 1
    for j in range(0, input[1] + 2, 1) :
        paper[j][0] = 1
        paper[j][input[0] + 1] = 1

def dfs(paper, garo, sero) :
    global temp
    if paper[sero][garo + 1] == 0 :
        paper[sero][garo + 1] = 1
        temp = temp + 1
        dfs(paper, garo + 1, sero)
    if paper[sero + 1][garo] == 0 :
        paper[sero + 1][garo] = 1
        temp = temp + 1
        dfs(paper, garo, sero + 1)
    if paper[sero][garo - 1] == 0 :
        paper[sero][garo - 1] = 1
        temp = temp + 1
        dfs(paper, garo - 1, sero)
    if paper[sero - 1][garo] == 0 :
        paper[sero - 1][garo] = 1
        temp = temp + 1
        dfs(paper, garo, sero - 1)

for i in range(input[2]) :
    xy = list(map(int, sys.stdin.readline().split()))
    # xy[0] = x1, xy[1] = y1
    # xy[2] = x2, xy[3] = y3
    for j in range(xy[0], xy[2], 1) :
        for k in range(xy[1], xy[3], 1) :
            paper[j + 1][k + 1] = 1

for i in range(1, input[1] + 2, 1) :
    for j in range(1, input[0] + 2, 1) :
        if paper[i][j] == 0 :
            count = count + 1
            temp = 1
            paper[i][j] = 1
            dfs(paper, j, i)
            territory.append(temp)

list.sort(territory)
print(count)
for i in territory :
    print(i, end=' ')