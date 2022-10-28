import itertools as it
n, m = map(int, input().split())
res = list(it.combinations([x for x in range(1, n + 1)], m))

for i in res:
    print(*i)