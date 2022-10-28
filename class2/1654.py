import sys
sys.stdin = open('./1654.txt')

k, n = map(int, input().split())
lines = []
for i in range(k):
    lines.append(int(input()))

start = 1
end = max(lines)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for line in lines:
        total += (line // mid)
    if total < n:
        end = mid - 1
    else:
        start = mid + 1
print(end)
