T = int(input())
for _ in range(T):
    R, S = input().split()
    ans = ""
    for i in S:
        ans += (i * int(R))
    print(ans)