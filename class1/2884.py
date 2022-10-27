H, M = map(int, input().split())

min_value = (H * 60) + M - 45
if min_value < 0:
    min_value += 1440
    print(min_value // 60 , min_value % 60)
else:
    print(min_value // 60 , min_value % 60)
 