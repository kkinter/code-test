M, N = map(int, input().split())
arr = set(range(2, N + 1))

for i in range(2, N + 1):
    if i in arr:
        arr -= set(range(i * 2, N + 1, i))

for j in sorted(list(arr)):
    if j in range(M, N + 1):
        print(j)

# m, n = map(int, input().split())
# if m == 1: m = 2
# num_set = set(range(m, n+1))
# for i in range(m, n+1):
#     for c in range(2, int(i**0.5)+1):
#         if i % c == 0:
#             num_set.remove(i)
#             break
# for i in num_set:
#     print(i)