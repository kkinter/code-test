import itertools

n, m = map(int, input().split())
# 10 ! / 3 ! * 7 !
# 10 * 9 * 8
# 3 * 2 * 1 * 

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = dp[i - 1]* i

print(dp[n] // (dp[m] * dp[n - m]))