from pprint import pprint

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    apart = [[0] * n for _ in range(k + 1)]
    zero_floor = [x for x in range(1, n + 1)]
    apart[0] = zero_floor
    for h in range(1, k + 1):
        for w in range(n):
            apart[h][w] = sum(apart[h-1][:w+1])

    print(apart[k][n - 1])