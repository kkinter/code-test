arr = 1
res = [0 for x in range(10)]
for _ in range(3):
    num = int(input())
    arr *= num
arr = str(arr)
for i in arr:
    res[int(i)] += 1
for j in res:
    print(j)