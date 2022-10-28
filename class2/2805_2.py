
n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees = sorted(trees)
start = 1
end = max(trees)
res = []
while start <= end:
    mid = (start + end) // 2

    length = 0
    for tree in trees:
        if tree > mid:
            length += tree - mid
    if length < m:
        end = mid - 1
    else:
        res = mid 
        start = mid + 1
print(end)