N = int(input())
num_arr = list(map(int, input().split()))
res = 0
for i in num_arr:
    is_prime = True
    if i == 1:
        continue
    else:
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
    if is_prime:
        res += 1

print(res)
    