import sys
sys.setrecursionlimit(1000000)

def dfs(lotto) :
    for i in range(0, input[0] - 5, 1) :
        for j in range(i + 1, input[0]- 4, 1) :
            for k in range(j + 1, input[0] - 3, 1) :
                for x in range(k + 1, input[0] - 2, 1) :
                    for y in range(x + 1, input[0]- 1, 1) :
                        for z in range(y + 1, input[0], 1) :
                            print(lotto[i], end=' ')
                            print(lotto[j], end=' ')
                            print(lotto[k], end=' ')
                            print(lotto[x], end=' ')
                            print(lotto[y], end=' ')
                            print(lotto[z])
                            if i == (input[0] - 6) and j == (input[0] - 5) and k == (input[0] - 4) and x == (input[0] - 3) and y == (input[0] - 2) and z == (input[0] - 1) :
                                return

while True :
    input = list(map(int, sys.stdin.readline().split()))
    lotto = []
    if input[0] == 0 :
        break
    else :
        for i in range(1, input[0] + 1, 1) :
            lotto.append(input[i])
    list.sort(lotto)
    dfs(lotto)
    print('')
