from collections import deque
import sys
# sys.stdin = open('./10866.txt')

input = sys.stdin.readline
N = int(input())

dq = deque([])
for i in range(N):
    arr = input().split()
    if len(arr) >= 2:
        command = arr[0]
        num = arr[1]
        if command == "push_back":
            dq.append(num)
        elif command == "push_front":
            dq.appendleft(num)
    else:
        command = arr[0]
        if command == "pop_front":
            if len(dq) >= 1:
                print(dq.popleft())
            else:
                print(-1)
        elif command == "pop_back":
            if len(dq) >= 1:
                print(dq.pop())
            else:
                print(-1)
        elif command == "size":
            print(len(dq))
        elif command == "empty":
            if len(dq) == 0:
                print(1)
            else:
                print(0)
        elif command == "front":
            if len(dq) >= 1:
                print(dq[0])
            else:
                print(-1)
        elif command == "back":
            if len(dq) >= 1:
                print(dq[-1])
            else:
                print(-1)
