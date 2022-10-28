import sys
sys.stdin = open('./11723.txt')
input = sys.stdin.readline
m = int(input())
s = set()
for i in range(m):
    arr = input().split()
    if len(arr) == 2:
        command = arr[0]
        n = int(arr[1])
        if command == "add":
            s.add(n)
        elif command == "remove":
            try:
                s.remove(n)
            except:
                pass
        elif command == "check":
            if n in s:
                print(1)
            else:
                print(0)
        elif command == "toggle":
            if n in s:
                s.remove(n)
            else:
                s.add(n)
    else:
        command = arr[0]
        if command == "all":
            s = set([x for x in range(1, 21)])
        elif command == "empty":
            s = set()
