import sys
from pprint import pprint
sys.stdin = open('./18111.txt')

N, M, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

used_blk = 0
time = 0
dicts = {}


for i in range(N):
    for j in range(M):
        if matrix[i][j] in dicts:
            dicts[matrix[i][j]] += 1
        else:
            dicts[matrix[i][j]] = 1
print(dicts)