import sys
from collections import deque

# sys.stdin = open('./1966.txt')

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    cnt = 0
    while queue:
        max_value = max(queue)
        front = queue.popleft()
        M -= 1

        if front == max_value:
            cnt += 1
            if M < 0:
                print(cnt)
                break
        else:
            queue.append(front)
            if M < 0:
                M = len(queue) - 1

