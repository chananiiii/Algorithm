'''
백준 1463번 - 1로 만들기

문제

정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
1.X가 3으로 나누어 떨어지면, 3으로 나눈다.
2.X가 2로 나누어 떨어지면, 2로 나눈다.
3.1을 뺀다.

정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
연산을 사용하는 횟수의 최솟값을 출력하시오.

입력

첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

출력

첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

예제 입력 1
 2
예제 출력 1
 1

예제 입력 2
 10
예제 출력 2 복사
 3
'''
import sys

input = int(sys.stdin.readline())
index = [0 for _ in range(input + 1)]
step = 1
index[1] = 0

def dp() :
    global index, input, step
    while True :
        if step == input :
            return index[step]

        if step + 1 < input + 1 and (index[step + 1] > index[step] or index[step + 1] == 0) :
            index[step + 1] = index[step] + 1

        if step * 2 < input + 1 and (index[step * 2] > index[step] or index[step * 2] == 0) :
            index[step * 2] = index[step] + 1

        if step * 3 < input + 1 and (index[step * 3] > index[step] or index[step * 3] == 0) :
            index[step * 3] = index[step] + 1

        step = step + 1
dp()
print(index[step])