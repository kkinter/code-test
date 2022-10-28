import sys
from collections import deque

sys.stdin = open('./1966.txt')

T = int(input())
# 중요도가 같으면, 순서대로 인쇄됨
for _ in range(T):
    N, M = map(int, input().split())
    p = list(map(int, input().split()))
    res = deque([])
    dicts = {}
    for i in range(N):
        dicts[i] = p[i]
        res.append((i, p[i]))

    arr = []
    # for t in res:
    #     max_val = max(res, key = lambda x:x[1])
    #     if t[1] == max_val[1]:
    #         res.pop(res.index(max_val))
    #     print(t[1])
    #     print(max_val)
    # print(res)
    # print("end")
    print(res)
    while res:
        for t in res:
            max_val = max(res, key = lambda x:x[1])
            
            if t[1] == max_val[1]:
                arr.append(t)
                res.popleft()
            else:
                res.append(res.popleft())
    print(arr)
    print(arr.index((M, p[M])))
    # arr = sorted(dicts.keys(), key = lambda x: (-dicts[x], x))
 
