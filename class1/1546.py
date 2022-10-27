N = int(input())
score_arr = list(map(int, input().split()))
M = max(score_arr)

res = 0
for score in score_arr:
    res += (score / M) * 100

print(res / N)