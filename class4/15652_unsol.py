import itertools as it
import sys
input = sys.stdin.readline
# https://juhee-maeng.tistory.com/91
n, m = map(int, input().split())
res = []
for i in it.product([x for x in range(1, n + 1)], repeat = m):
    if tuple(sorted(i)) not in res:
        res.append(i)
        print(*i)

