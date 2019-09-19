import sys

testcase = int(sys.stdin.readline())
for _ in range(testcase) :
    count = 0
    number = int(sys.stdin.readline())
    prison = [0 for _ in range(number + 1)]
    for i in range(1, number + 1) :
        for j in range(i, number + 1, i) :
            if prison[j] == 0 :
                prison[j] = 1
            else :
                prison[j] = 0
        if prison[i] == 1 :
            count += 1
    print(count)