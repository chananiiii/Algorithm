'''
백준 11724번 - 연결 요소의 개수
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
(1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
(1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

예제 입력 1
6 5
1 2
2 5
5 1
3 4
4 6

예제 출력 1
2
'''
import sys
sys.setrecursionlimit(1000000)
count = 0
a = list(map(int, sys.stdin.readline().split()))
graph = [[0] * a[0] for i in range(a[0])]
check = [0 for i in range(a[0])]
for i in range(a[1]) :
    b = list(map(int, sys.stdin.readline().split()))
    graph[b[0] - 1][b[1] - 1] = 1
    graph[b[1] - 1][b[0] - 1] = 1

def dfs(current) :
    for i in range(a[0]) :
        if graph[current][i] is 1 :
            if check[i] is 1 :
                continue
            if check[i] is 0 :
                check[i] = 1
                dfs(i)

for i in range(a[0]) :
    if check[i] is 0 :
        check[i] = 1
        count = count + 1
        dfs(i)

print(count)