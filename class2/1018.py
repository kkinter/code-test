import sys
from pprint import pprint
sys.stdin = open('./1018.txt')

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

res = 100001

# 조회 해야하는 체스판이 8 * 8 로 정해짐
for h in range(N - 7):
    for w in range(M - 7):
        # arr[0][0] 이 "W" 일 때, 혹은 "B" 일 때 저장하기 위한 변수 선언
        idx_1 = 0
        idx_2 = 0
        for i in range(h, h + 8):
            for j in range(w, w + 8):
                if ( i + j ) % 2 == 0:
                    if arr[i][j] != 'B':
                        idx_1 += 1
                    if arr[i][j] != 'W':
                        idx_2 += 1
                else:
                    if arr[i][j] != 'W':
                        idx_1 += 1
                    if arr[i][j] != 'B':
                        idx_2 += 1
        res = min(res, idx_1, idx_2)   

print(res)
            
