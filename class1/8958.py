T = int(input())
for _ in range(T):
    arr = input()
    ans = 0
    arr = arr.split("X")
    for i in arr:
        length = len(i)
        ans += (length*(length + 1)) // 2
    print(ans)