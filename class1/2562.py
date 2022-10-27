arr = []

for i in range(9):
    num = int(input())
    arr.append(num)
    
max_num = max(arr)
idx = arr.index(max_num)

print(max_num)
print(idx + 1)

    
