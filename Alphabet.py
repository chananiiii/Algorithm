'''
백준 문제 1987
세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다.
보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.
말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데,
새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다.
즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.
좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오.
말이 지나는 칸은 좌측 상단의 칸도 포함된다.

입력
첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1<=R,C<=20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.

예제 입력 1
2 4
CAAB
ADCB

예제 출력 1
3
'''

import sys

sys.setrecursionlimit(1000000)
input = list(map(int, sys.stdin.readline().split()))
board = [[0] * input[1] for i in range(0, input[0], 1)]
# input[0] = sero, input[1] = garo
maximum = 0

def dfs(board, garo, sero, tempMaximum) :
    global maximum
    global passAlphabet
    if maximum < tempMaximum :
        maximum = tempMaximum

    if garo + 1 < input[1] and passAlphabet[ord(board[sero][garo + 1])] == 0 :
        passAlphabet[ord(board[sero][garo + 1])] = 1
        dfs(board, garo + 1, sero, tempMaximum + 1)
        passAlphabet[ord(board[sero][garo + 1])] = 0

    if sero + 1 < input[0] and passAlphabet[ord(board[sero + 1][garo])] == 0 :
        passAlphabet[ord(board[sero + 1][garo])] = 1
        dfs(board, garo, sero + 1, tempMaximum + 1)
        passAlphabet[ord(board[sero + 1][garo])] = 0

    if garo - 1 > -1 and passAlphabet[ord(board[sero][garo - 1])] == 0 :
        passAlphabet[ord(board[sero][garo - 1])] = 1
        dfs(board, garo - 1, sero, tempMaximum + 1)
        passAlphabet[ord(board[sero][garo - 1])] = 0

    if sero - 1 > -1 and passAlphabet[ord(board[sero - 1][garo])] == 0 :
        passAlphabet[ord(board[sero - 1][garo])] = 1
        dfs(board, garo, sero - 1, tempMaximum + 1)
        passAlphabet[ord(board[sero - 1][garo])] = 0

for i in range(0, input[0], 1) :
    str = sys.stdin.readline()
    for j in range(0, input[1], 1) :
        board[i][j] = str[j]

passAlphabet = [0 for i in range(0, 100, 1)]
passAlphabet[ord(board[0][0])] = 1
maximum = maximum + 1
dfs(board, 0, 0, 1)
print(maximum)