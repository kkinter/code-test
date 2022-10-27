import sys
from pprint import pprint
sys.stdin = open('./1018.txt')

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

ans = 0

for i in range(8):
    for j in range(8):
        for k in range(4):
            nx = dx[k] + j
            ny = dy[k] + i
            try:
                if arr[ny][nx] == arr[i][j]:
                    if arr[ny][nx] == 'W':
                        arr[ny][nx] = 'B'
                        ans += 1
                    elif arr[ny][nx] == 'B':
                        arr[ny][nx] = 'W'
                        ans += 1
            except:
                pass
print(ans)
pprint(arr)