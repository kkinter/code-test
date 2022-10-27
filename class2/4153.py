while True:
    arr = sorted(list(map(int, input().split())))
    if arr[0] == 0 and arr[1] == 0 and arr[2] == 0:
        break
    if arr[2] * arr[2] == arr[1] * arr[1] + arr[0] * arr[0]:
        print("right")
    else:
        print("wrong")