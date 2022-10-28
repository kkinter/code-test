arr = [1, 3, 5, 7, 8, 11, 13, 15, 17, 19]
print(arr)
# def binary(arr, start, end, target):
#     if start > end:
#         return None
    
#     mid = (start + end) // 2
    
#     if arr[mid] == target:
#         return mid
    
#     elif arr[mid] > target:
#         binary(arr, start, mid - 1, target)
#     else:
#         binary(arr, mid + 1, end, target)

# print(binary(arr, 0, len(arr) - 1, 7))

def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)

print(binary_search(arr, 7, 0, 9))

start = 0
m = 20
arr = [19, 14, 10, 17]
end = max(arr)
res = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in arr:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        res = mid
        start = mid + 1
        