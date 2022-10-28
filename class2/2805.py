n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
# 1. start > end : return None
# 2. mid = start // 2
# 3. target == arr[mid] : return mid
# 4. if arr[mid] > target : start = 0 end = mid
res = []
while start <= end:
    total = 0
    mid = (start + end) // 2
    print(mid)
    for h in trees:
        if h > mid:
            total += h - mid
    if total < m:
        end = mid - 1
    else:
        res = mid
        start = mid + 1

print(res)