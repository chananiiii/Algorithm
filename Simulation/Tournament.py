import sys
import queue

people, kim, im = map(int, sys.stdin.readline().split())

deque = queue.deque()
for i in range(people) :
    if i == kim - 1 or i == im - 1:
        deque.append([1, i])
    else :
        deque.append([0, i])

round = 0
done = 0
while len(deque) != 1:
    if done == 1 :
        break
    temp = 0
    round += 1
    if len(deque) % 2 == 0 :
        temp = int(len(deque) / 2)
        for i in range(temp) :
            a1, b1 = deque.popleft()
            a2, b2 = deque.popleft()
            if a1 == 0 and a2 == 0 :
                deque.append([a1, b1])
            if a1 == 1 :
                deque.append([a1, b1])
            if a2 == 1 :
                deque.append([a2, b2])
            if a1 == 1 and a2 == 1 :
                i = temp
                done = 1
    else :
        temp = int(len(deque) / 2)
        for i in range(temp) :
            a1, b1 = deque.popleft()
            a2, b2 = deque.popleft()
            if a1 == 0 and a2 == 0 :
                deque.append([a1, b1])
            if a1 == 1 :
                deque.append([a1, b1])
            if a2 == 1 :
                deque.append([a2, b2])
            if a1 == 1 and a2 == 1 :
                while len(deque) == 0 :
                    deque.popleft()
                i = temp
                done = 1
        deque.append(deque.popleft())

print(round)