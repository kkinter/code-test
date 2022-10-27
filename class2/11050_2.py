import itertools

n, k = map(int, input().split())
arr = [x for x in range(1, n + 1)]
res = list(itertools.combinations(arr, k))
print(len(res))