import sys

num = int(sys.stdin.readline())
array = [0 for _ in range(num)]
dp1 = [1 for _ in range(num)]
dp2 = [1 for _ in range(num)]
temp = list(map(int, sys.stdin.readline().split()))
for i in range(num) :
    array[i] = temp[i]

maximum = 0
for i in range(1, num) :
    for j in range(0, i) :
        if array[j] < array[i] :
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(num - 2, -1, -1) :
    for j in range(num - 1, i, - 1) :
        if array[i] > array[j] :
            dp2[i] = max(dp2[i], dp2[j] + 1)

maximum = 0
for i in range(num) :
    maximum = max(maximum, dp1[i] + dp2[i] - 1)

print(maximum)