from collections import deque
import sys

# sys.stdin = open('./10845.txt')
input = sys.stdin.readline
N = int(input())

que = deque([])
for i in range(N):
    arr = input().split()
    if len(arr) >= 2:
        command = arr[0]
        num = arr[1]
        if command == "push":
            que.append(num)
        

    else:
        command = arr[0]
        if command == "pop":
            if len(que) >= 1:
                print(que.popleft())
            else:
                print(-1)
        elif command == "size":
            print(len(que))
        elif command == "empty":
            if len(que) >= 1:
                print("0")
            else:
                print("1")
        elif command == "front":
            if len(que) >= 1:
                print(que[0])
            else:
                print(-1)
        elif command == "back":
            if len(que) >= 1:
                print(que[-1])
            else:
                print(-1)

            