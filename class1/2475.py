num_arr = list(map(int, input().split()))
sum_val = 0
for num in num_arr:
    sum_val += num * num
print(sum_val % 10)    